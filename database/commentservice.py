from datetime import datetime

from database import get_db
# from database import Comment

from database.models import Comment


# Опубликовать комментарий
def add_comment_db(post_id, text, user_id):
    db = next(get_db())

    new_comment = Comment(user_id=user_id,
                          comment_text=text,
                          post_id=post_id)

    # Добавить запись в бд
    db.add(new_comment)
    db.commit()

    return "Комментарий успешно добавлен"


# Удалить комментарий
def delete_comment_id(comment_id):
    db = next(get_db())

    exact_comment = db.query(Comment).filter_by(id=comment_id).first()

    if exact_comment:
        db.delete(exact_comment)
        db.commit()

        return 'Успешно удалено'

    return False


# Изменить определённый комментарий
def change_comment_db(comment_id, new_comment):
    db = next(get_db())

    exact_comment = db.query(Comment).filter_by(id=comment_id).first()

    if exact_comment:
        exact_comment.comment_text = new_comment
        db.commit()

        return 'Успешно изменено'

    return False


# Получить все комменты определенного поста
def get_post_comments(post_id):
    db = next(get_db())

    exact_post_comments = db.query(Comment).filter_by(post_id=post_id).all()

    return exact_post_comments
