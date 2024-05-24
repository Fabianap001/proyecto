from .entities.User import User

# @classmethod
# class ModelUser():
#     def login(self,db,user):
#         try:
#             cursor=db.connection.cursor()
#             sql="""SELECT id, username, password, fullname FROM user" WHERE username = '{}'""".format(user.username)
#             cursor.execute(sql)
#             row=cursor.fetchone()
#             if row != None:
#                 user = User(row[0], row[1], User.check_password(row[2], user.password), row[3])
#             else:
#                 return None
#         except Exception as ex:
#             raise Exception(ex)


class ModelUser:
    @staticmethod
    def login(db, user):
        try:
            cursor = db.connection.cursor()
            sql = "SELECT id, inputUsername, inputPassword, fullname FROM user WHERE username = %s"
            cursor.execute(sql, (user.username,))
            row = cursor.fetchone()
            if row is not None:
                user_id, username, hashed_password, fullname = row
                if User.check_password(hashed_password, user.password):
                    return User(user_id, username, fullname)
                else:
                    return None
            else:
                return None
        except Exception as ex:
            print("Error during login:", ex)
            return None
