from sqlalchemy.orm import Mapper, Session
from sqlalchemy.orm.attributes import InstrumentedAttribute
from sqlalchemy import or_
from sqlalchemy.exc import NoResultFound
from fastapi import APIRouter, Depends, UploadFile, Form, Path, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel
from typing import Any, Union, List, TypeVar, Generic, Annotated, Optional
from database.pagination import paginate
from routes.handlers_str import (get_handler_str, post_handler_str, post_handler_file_str,
                                delete_handler_str, put_handler_file_str, put_handler_str)
from datetime import date, datetime
from database.file_handler import UploadFileHandler
import runpy
import os


def dependency_factory(obj) :

    return lambda : obj


def import_schemas() :

    script_dict = runpy.run_path('schemas/schema_importer.py')
    schemas_dict = {}
    for k, v in script_dict.items() :
        if 'schema' in k.lower() :
            schemas_dict[k] = v
    globals().update(schemas_dict)


import_schemas()
Type = TypeVar("Type")


class ResponseGet(BaseModel, Generic[Type]):
    has_next: bool
    has_previous: bool
    pages: int
    total: int
    next_page: Union[int, None]
    previous_page: Union[int, None]
    items: List[Type]


class CRUDRouter(APIRouter) :
    """
    `CRUDRouter` is a generic CRUD routes generator for any model
    """

    def __init__(self, schema: BaseModel, schema_detailed: BaseModel, create_schema: BaseModel,
                 update_schema: BaseModel, db_session: Any, db_model: Mapper, prefix: str, 
                 page_size: int, file_path: str='media') -> None :
        
        self.schema = schema
        self.schema_detailed = schema_detailed
        self.create_schema = create_schema
        self.update_schema = update_schema
        self.prefix = prefix
        self.page_size = page_size
        self.db_session = db_session
        self.db_model = db_model
        self.file_handler = UploadFileHandler(file_path)

        if not prefix.startswith("/"):
            prefix = "/" + prefix

        self.prefix = prefix

        super().__init__(prefix=self.prefix)
        # CRUD
        self.create_routes()

    
    def create_routes(self) :

        self.get_add()
        self.post_add()
        self.delete_add()
        self.put_add()


    def get_add(self) -> None :

        self.add_api_route(
            '',
            endpoint=self.get_handler(),
            methods=['GET'],
            response_model=ResponseGet[self.schema],
        )
        self.add_api_route(
            '/detailed',
            endpoint=self.get_handler(),
            methods=['GET'],
            response_model=ResponseGet[self.schema_detailed],
        )
        if self.has_file() :
            self.add_api_route(
                '/file/{id}',
                endpoint=self.get_file_handler(),
                methods=['GET'],
            )

    
    def post_add(self) -> None :

        self.add_api_route(
            '',
            endpoint=self.post_handler(),
            methods=['POST'],
            response_model=self.schema
        )


    def delete_add(self) -> None : 

        self.add_api_route(
            '',
            endpoint=self.delete_handler(),
            methods=['DELETE']
        )

    
    def put_add(self) -> None :

        self.add_api_route(
            '/{id}',
            endpoint=self.put_handler(),
            methods=['PUT'],
            response_model=self.schema
        )


    def get_handler(self) :

        param, params_v, _ = self.get_params()
        local_dict = {'obj': self, 'keys': dependency_factory(params_v)}
        exec(get_handler_str(param), globals(), local_dict)
        return locals()['local_dict']['handler']


    def get_file_handler(self) :

        def handler(id: int, db: Session=Depends(self.db_session)) :
            model = db.query(self.db_model).filter(self.db_model.id == id).first()
            if not model:
                return HTTPException(status_code=404, detail="File not found")
            file_path = model.chemin_fichier
            if not os.path.exists(file_path):
                return HTTPException(status_code=404, detail="File not found")
            return FileResponse(file_path)
        return handler

    

    def post_handler(self) :
        
        param, params_v, _ = self.post_with_file_params()
        local_dict = {'obj': self, 'keys': dependency_factory(params_v)}
    
        if self.has_file() :
            exec(post_handler_file_str(param), globals(), local_dict)
        else :
            schema_name = str(self.create_schema).strip("'>").split('.')[-1]
            exec(post_handler_str(schema_name), globals(), local_dict)
        return locals()['local_dict']['handler']
    

    def delete_handler(self) :

        local_dict = {'obj': self}
        exec(delete_handler_str(), globals(), local_dict)
        return locals()['local_dict']['handler']
    

    def put_handler(self) :

        param, params_v, _ = self.put_with_file_params()
        local_dict = {'obj': self, 'keys': dependency_factory(params_v)}
    
        if self.has_file(True) :
            exec(put_handler_file_str(param), globals(), local_dict)
        else :
            schema_name = str(self.update_schema).strip("'>").split('.')[-1]
            exec(put_handler_str(schema_name), globals(), local_dict)
        return locals()['local_dict']['handler']
    
    
    def has_file(self, use_update: bool=False) -> bool :

        if use_update :
            schema = self.update_schema
        else :
            schema = self.create_schema

        for field_name in schema.model_fields :
            type_field = schema.model_fields[field_name].annotation
            if type_field in [UploadFile, Optional[UploadFile]] :
                return True
        return False
    

    def with_file_params(self, params_v: List, params_t: List, use_none=False) :

        none_type = ''
        default_value = ''
        if use_none :
            none_type = ' | None'
            default_value = ' = None'

        params = []
        for v, t in zip(params_v, params_t) :
            if t != 'UploadFile' :
                params.append(f"{v}: Annotated[{t}{none_type}, Form()]{default_value}")
            else :
                params.append(f"{v}: UploadFile | None=None")
        return ' , '.join(params), params_v, params_t


    def put_with_file_params(self) :
    
        params_v = []
        params_t = []

        for field_name in self.update_schema.model_fields :

            type_field = self.update_schema.model_fields[field_name].annotation
            if type_field == Optional[str] :
                self.add_param(params_v, params_t, field_name, 'str')

            elif type_field == Optional[int] :
                self.add_param(params_v, params_t, field_name, 'int')

            elif type_field == Optional[bool] : 
                self.add_param(params_v, params_t, field_name, 'bool')

            elif type_field == Optional[date] :
                self.add_param(params_v, params_t, field_name, 'date')

            elif type_field == Optional[UploadFile] :
                self.add_param(params_v, params_t, field_name, 'UploadFile')

            elif type_field == Optional[datetime] :
                self.add_param(params_v, params_t, field_name, 'datetime')


        return self.with_file_params(params_v, params_t, True)


    def post_with_file_params(self) :

        params_v, params_t = self.value_type_fields(True, True)
        return self.with_file_params(params_v, params_t)
        
    

    def get_params(self) -> str:

        params = []
        params_v, params_t = self.value_type_fields()
        
        for v, t in zip(params_v, params_t) :
            params.append(f"{v}: {t} | None=None")
        return ' ,'.join(params), params_v, params_t
    

    def value_type_fields(self, include_file: bool=False, use_create: bool=False) :

        if use_create :
            schema = self.create_schema
        else :
            schema = self.schema

        params_v = []
        params_t = []

        for field_name in schema.model_fields :

            type_field = schema.model_fields[field_name].annotation
            if type_field == str :
                self.add_param(params_v, params_t, field_name, 'str')

            elif type_field == int or type_field == Optional[int] :
                self.add_param(params_v, params_t, field_name, 'int')

            elif type_field == bool : 
                self.add_param(params_v, params_t, field_name, 'bool')

            elif type_field == date :
                self.add_param(params_v, params_t, field_name, 'date')
            
            elif type_field == datetime :
                self.add_param(params_v, params_t, field_name, 'datetime')

            elif type_field == UploadFile :
                if include_file :
                    self.add_param(params_v, params_t, field_name, 'UploadFile')

        return params_v, params_t
        

    def add_param(self, params_v: List, params_t: List, value: str, type: str) :
        params_v.append(value)
        params_t.append(type)
        

    def __hash__(self) :
        return hash(self.prefix)
    

    def __call__(self) :
        return self

