
def get_handler_str(param: str) :

    return f'''
obj = locals()['obj']
keys = locals()['keys']
def handler(db: Session = Depends(obj.db_session),
            obj: CRUDRouter = Depends(obj),
            keys: List = Depends(keys),
            {param},
            page: int=1,
            page_size: int=10,
            search: str=''
        ):

        query = db.query(obj.db_model)

        # Filter by column value
        for k in keys :
            val = locals()[k]
            if  val != None :
                if isinstance(val, str) :
                    query = query.filter(obj.db_model.__dict__[k].like('%' + val + '%'))
                else :
                    query = query.filter(obj.db_model.__dict__[k] == val)

        # Filter by search pattern
        # Only doing on integer and string
        if search :
            conditions = []

            for item in obj.db_model.__dict__.items() :
                if isinstance(item[1], InstrumentedAttribute) :
                
                    if item[0] == 'id' :
                        continue
                
                    try :
                        col_py_type = obj.db_model.__dict__[item[0]].type.python_type
                    except AttributeError :
                        col_py_type = None
                        
                    if col_py_type == int :
                        try :
                            int_search = int(search)
                            conditions.append(obj.db_model.__dict__[item[0]] == int_search)
                        except ValueError :
                            pass
                    elif col_py_type == str :
                        conditions.append(obj.db_model.__dict__[item[0]].like('%' + search +'%'))

            query = query.filter(or_(*conditions))
        
        if obj.page_size and obj.page_size >= 1 :
            page_size = obj.page_size

        page = paginate(query, page, page_size)
        return page
        '''


def post_handler_file_str(param: str) :

    return f'''
obj = locals()['obj']
keys = locals()['keys']
def handler({param},
            db: Session = Depends(obj.db_session),
            obj: CRUDRouter = Depends(obj),
            keys: List = Depends(keys)
        ):

            file = locals()['fichier']
            model = obj.db_model()
            for k in keys :
                if 'fichier' not in k :
                    val = locals()[k]
                    if val != None :
                        setattr(model, k, val)
        
            model.chemin_fichier = obj.file_handler.save(file)

            db.add(model)
            db.commit()
                    
            return model
        '''


def post_handler_str(schema_name: str) :
    
    return f'''
obj = locals()['obj']
keys = locals()['keys']
def handler(in_data: {schema_name},
            db: Session = Depends(obj.db_session),
            obj: CRUDRouter = Depends(obj),
            keys: List = Depends(keys)
        ):

            model = obj.db_model()
            for k in keys :
                setattr(model, k, in_data.__dict__[k])
            db.add(model)
            db.commit()
                    
            return model
        '''


def delete_handler_str() :
    
    return '''
obj = locals()['obj']
def handler(db: Session = Depends(obj.db_session),
            obj: CRUDRouter = Depends(obj),
            id: str | None = None
        ):

            if id == None :
                for row in db.query(obj.db_model).all() :
                    if row :
                        obj.file_handler.remove(row)
                        db.delete(row)
                db.commit()
                return {'details': 'All deleted successfully!'}              
            else :
                ids = map(lambda x: int(x), id.split('_'))
                for _id in list(ids) :
                    row = db.query(obj.db_model).filter(obj.db_model.id == _id).first() 
                    if row : 
                        obj.file_handler.remove(row)
                        db.delete(row)
                db.commit()
                return {'details': 'Deleted successfuly'}
        '''


def put_handler_file_str(param: str) :

    return f'''
obj = locals()['obj']
keys = locals()['keys']
def handler(id: Annotated[int, Path(title='id of element')],
            {param},
            db: Session = Depends(obj.db_session),
            obj: CRUDRouter = Depends(obj),
            keys: List = Depends(keys)
        ) :

            file = locals()['fichier']
            try :
                model = db.query(obj.db_model).filter(obj.db_model.id == id).one()
                for k in keys :
                    if 'fichier' not in k :
                        val = locals()[k]
                        if val :
                            setattr(model, k, val)

            except NoResultFound :
                raise HTTPException(status_code=404, detail='Element does not exists')

            if file :
                model.chemin_fichier = obj.file_handler.save(file, model.chemin_fichier)
                    
            return model
        '''


def put_handler_str(schema_name: str) :
        
    return f'''
obj = locals()['obj']
keys = locals()['keys']
def handler(in_data: {schema_name},
            id: Annotated[int, Path(title='id of element')],
            db: Session = Depends(obj.db_session),
            obj: CRUDRouter = Depends(obj),
            keys: List = Depends(keys),
        ) :

            model = db.query(obj.db_model).filter(obj.db_model.id == id).one()
            for k in keys :
                if in_data.__dict__[k] :
                    setattr(model, k, in_data.__dict__[k])
            
            db.commit()
                    
            return model
        '''

