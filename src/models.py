from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

db = SQLAlchemy()
class Instagram_user(db.Model):
    _tablename_ = 'instagram_user'
    id: Mapped[int] = mapped_column(primary_key = True)
    username: Mapped[str] = mapped_column(String(25), nullable= False, unique = True)
    firstname: Mapped[str] = mapped_column(String(25), nullable= False)
    lastname: Mapped[str] = mapped_column(String(25), nullable= False)
    email: Mapped[str] = mapped_column(String(50), unique= True)
    comments: Mapped[list['Instagram_comment']] = relationship(back_populates= 'comment_by')

class Instagram_media(db.Model):
    _tablename_ = 'instagram_media'
    id: Mapped[int] = mapped_column(primary_key = True)
    type: Mapped[str] = mapped_column(String(50))
    url: Mapped[str] = mapped_column(String(50), unique = True)
    post_id: Mapped[int] = mapped_column(ForeignKey('instagram_post.id'))
    
class Instagram_comment(db.Model):
    _tablename_ = 'instagram_comment'
    id: Mapped[int] = mapped_column(primary_key = True)
    comment_text: Mapped[str] = mapped_column(String(100), nullable = False)
    author_id: Mapped[int] = mapped_column(ForeignKey('instagram_user.id'))
    comment_by: Mapped['Instagram_user'] = relationship(back_populates= 'comments')
    post_id: Mapped[int] = mapped_column(ForeignKey('instagram_post.id'))
    post: Mapped['Instagram_post'] = relationship(back_populates = 'comentarios')

class Instagram_post(db.Model):
    _tablename_ = 'instagram_post'
    id: Mapped[int] = mapped_column(primary_key = True)
    user_id:  Mapped[int] = mapped_column(ForeignKey('instagram_user.id'))
    comentarios: Mapped[list['Instagram_comment']] = relationship(back_populates = 'post') 

class Instagram_followers(db.Model):
    _tablename_ = 'instagram_followers'
    id: Mapped[int] = mapped_column(primary_key = True)
    user_from_id: Mapped[int] = mapped_column(ForeignKey('instagram_user.id'))

    user_to_id: Mapped[int] = mapped_column(ForeignKey('instagram_user.id'))



class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)


    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }
