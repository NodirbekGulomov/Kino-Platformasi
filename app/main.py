from decimal import Decimal
import json

from sqlalchemy import Integer, Numeric, create_engine, delete, func, or_, select, update
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column


class Base(DeclarativeBase):
    pass


engine = create_engine("sqlite:///kino.db")


class Movie(Base):
    __tablename__ = 'movies'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    title: Mapped[str]
    genre: Mapped[str]
    release_year: Mapped[int]
    duration: Mapped[int]
    rating: Mapped[Decimal] = mapped_column(Numeric(precision=3, scale=1))
    director: Mapped[str]


Base.metadata.create_all(bind=engine)


def load_initial_data():
    with open('data.json', 'r') as file:
        movies = json.load(file)

    with Session(engine) as session:
        movies_objects = [
            Movie(
                title=item['title'],
                genre=item['genre'],
                release_year=item['release_year'],
                duration=item['duration'],
                rating=item['rating'],
                director=item['director'],
            ) for item in movies
        ]

    session.execute(delete(Movie))

    session.add_all(movies_objects)
    session.commit()


load_initial_data()


# 1. Barcha kinolarni chiqarib bering.
def t1():
    with Session(engine) as session:
        stmt = select(Movie)
        res = session.execute(stmt).scalars().all()
        for item in res:
            print(item.id, item.title, sep=' | ')


# t1()

# 2. Faqat genre = "Sci-Fi" bo‘lgan kinolarni chiqaring.
def t2():
    with Session(engine) as session:
        stmt = select(Movie).where(Movie.genre == 'Sci-Fi')
        res = session.execute(stmt).scalars().all()
        for item in res:
            print(item.title, item.genre)


# t2()

# 3. release_year > 2015 bo‘lgan kinolarni chiqaring.
def t3():
    with Session(engine) as session:
        stmt = select(Movie).where(Movie.release_year > 2015)
        res = session.execute(stmt).scalars().all()
        for item in res:
            print(item.title, item.release_year)


# t3()

# 4. rating >= 8.5 bo‘lgan kinolarni chiqaring.
def t4():
    with Session(engine) as session:
        stmt = select(Movie).where(Movie.rating >= Decimal("8.5"))
        res = session.execute(stmt).scalars().all()
        for item in res:
            print(item.title, item.rating)


# t4()

# 5. duration > 150 bo‘lgan kinolarni chiqaring.
def t5():
    with Session(engine) as session:
        stmt = select(Movie).where(Movie.duration > 150)
        res = session.execute(stmt).scalars().all()
        for item in res:
            print(item.title, item.duration)


# t5()

# 6. Faqat director = "Christopher Nolan" bo‘lgan kinolarni chiqaring.
def t6():
    with Session(engine) as session:
        stmt = select(Movie).where(Movie.director == 'Christopher Nolan')
        res = session.execute(stmt).scalars().all()
        for item in res:
            print(item.title, item.director)


# t6()

# 7. genre = "Action" VA rating > 7.5 bo‘lgan kinolarni chiqaring.
def t7():
    with Session(engine) as session:
        stmt = select(Movie).where(Movie.genre == 'Action', Movie.rating > Decimal('7.5'))
        res = session.execute(stmt).scalars().all()
        for item in res:
            print(item.title, item.genre, item.rating, sep=' | ')


# t7()

# 8. director = "James Cameron" YOKI director = "Christopher Nolan" bo‘lgan kinolarni chiqaring.
def t8():
    with Session(engine) as session:
        stmt = select(Movie).where(or_(Movie.director == 'James Cameron', Movie.director == 'Christopher Nolan'))
        res = session.execute(stmt).scalars().all()
        for item in res:
            print(item.title, item.director)


# t8()

# 9. genre IN ("Thriller", "Drama") bo‘lgan kinolarni chiqaring.
def t9():
    with Session(engine) as session:
        stmt = select(Movie).where(Movie.genre.in_(['Thriller', 'Drama']))
        res = session.execute(stmt).scalars().all()
        for item in res:
            print(item.title, item.genre)


# t9()

# 10. Nomida "man" so‘zi qatnashgan kinolarni chiqaring.
def t10():
    with Session(engine) as session:
        stmt = select(Movie).where(Movie.title.ilike(r"%man%"))
        res = session.execute(stmt).scalars().all()
        for item in res:
            print(item.title)


# t10()

# 11. Nomi "r" harfi bilan tugaydigan kinolarni chiqaring.
def t11():
    with Session(engine) as session:
        stmt = select(Movie).where(Movie.title.ilike(r'%r'))
        res = session.execute(stmt).scalars().all()
        for item in res:
            print(item.title)


# t11()

# 12. Nomi "The" bilan boshlanadigan kinolarni chiqaring.
def t12():
    with Session(engine) as session:
        stmt = select(Movie).where(Movie.title.ilike(r'the%'))
        res = session.execute(stmt).scalars().all()
        for item in res:
            print(item.title)


# t12()

# 13. release_year BETWEEN 2010 AND 2020 bo‘lgan kinolarni chiqaring.
def t13():
    with Session(engine) as session:
        stmt = select(Movie).where(Movie.release_year.between(2010, 2020))
        res = session.execute(stmt).scalars().all()
        for item in res:
            print(item.title, item.release_year)


# t13()

# 14. Kinolarni rating bo‘yicha kamayish tartibida chiqaring.
def t14():
    with Session(engine) as session:
        stmt = select(Movie).order_by(Movie.rating.desc())
        res = session.execute(stmt).scalars().all()
        for item in res:
            print(item.title, item.rating)


# t14()

# 15. Kinolarni release_year bo‘yicha o‘sish tartibida chiqaring.
def t15():
    with Session(engine) as session:
        stmt = select(Movie).order_by(Movie.release_year)
        res = session.execute(stmt).scalars().all()
        for item in res:
            print(item.title, item.release_year)


# t15()

# 16. Eng uzun davomiylikka ega 3 ta kinoni chiqaring.
def t16():
    with Session(engine) as session:
        stmt = select(Movie).order_by(Movie.duration.desc()).limit(3)
        res = session.execute(stmt).scalars().all()
        for item in res:
            print(item.title, item.duration)


# t16()


# 17. Dastlabki 4 ta kinoni chiqaring.
def t17():
    with Session(engine) as session:
        stmt = select(Movie).order_by(Movie.release_year).limit(4)
        res = session.execute(stmt).scalars().all()
        for item in res:
            print(item.title, item.release_year)


# t17()

# 18. 2 ta kinoni tashlab, keyingi 5 tasini chiqaring (offset + limit).
def t18():
    with Session(engine) as session:
        stmt = select(Movie).offset(2).limit(5)
        res = session.execute(stmt).scalars().all()
        for item in res:
            print(item.title)


# t18()

# 19. Jadvaldagi jami kinolar sonini aniqlang.
def t19():
    with Session(engine) as session:
        stmt = select(func.count(Movie.id))
        res = session.execute(stmt).scalar_one_or_none()

        print(res)


# t19()

# 20. Eng yuqori ratingga ega kino ratingini aniqlang.
def t20():
    with Session(engine) as session:
        stmt = select(func.max(Movie.rating))
        res = session.execute(stmt).scalar_one_or_none()

        print(res)


# t20()


# 21. Eng eski kino yilini aniqlang.
def t21():
    with Session(engine) as session:
        stmt = select(func.min(Movie.release_year))
        res = session.execute(stmt).scalar_one_or_none()
        print(res)


# t21()

# 22. Kinolarning o‘rtacha rating qiymatini aniqlang.
def t22():
    with Session(engine) as session:
        stmt = select(func.avg(Movie.rating))
        res = session.execute(stmt).scalar_one_or_none()
        print(res)


# t22()

# 23. Barcha kinolar davomiyligining (duration) jami yig‘indisini aniqlang.
def t23():
    with Session(engine) as session:
        stmt = select(func.sum(Movie.duration))
        res = session.execute(stmt).scalar_one_or_none()
        print(res)


# t23()

# 24. genre bo‘yicha guruhlab, har bir janrda nechta kino borligini chiqaring.
def t24():
    with Session(engine) as session:
        stmt = select(Movie.genre, func.count(Movie.id)).group_by(Movie.genre)
        res = session.execute(stmt).all()
        for item in res:
            print(item)


# t24()

# 25. director bo‘yicha guruhlab, o‘rtacha ratingni chiqaring.
def t25():
    with Session(engine) as session:
        stmt = select(Movie.director, func.avg(Movie.rating)).group_by(Movie.director)
        res = session.execute(stmt).all()
        for item in res:
            print(item)


# t25()

# 26. rating < 8.0 bo‘lgan kinolarni toping.
def t26():
    with Session(engine) as session:
        stmt = select(Movie).where(Movie.rating < Decimal("8.0"))
        res = session.execute(stmt).scalars().all()
        for item in res:
            print(item.title, item.rating)


# t26()


# 27. title = "Dune" bo‘lgan kinoning rating qiymatini 8.3 ga o‘zgartiring.
def t27():
    with Session(engine) as session:
        stmt = update(Movie).where(Movie.title == 'Dune').values(rating=Decimal('8.3'))
        session.execute(stmt)
        session.commit()


# t27()

# 28. director = "Christopher Nolan" bo‘lgan barcha kinolarning rating qiymatini 0.1 ga oshiring.
def t28():
    with Session(engine) as session:
        stmt = update(Movie).where(Movie.director == 'Christopher Nolan').values(rating=Movie.rating + Decimal('0.1'))
        session.execute(stmt)
        session.commit()


# t28()

# 29. release_year < 2005 bo‘lgan barcha kinolarni o‘chirib tashlang.
def t29():
    with Session(engine) as session:
        stmt = delete(Movie).where(Movie.release_year < 2005)
        session.execute(stmt)
        session.commit()


# t29()

# 30. genre = "Sci-Fi" bo‘lgan kinolarning davomiyligini 10 daqiqaga oshiring.
def t30():
    with Session(engine) as session:
        stmt = update(Movie).where(Movie.genre == 'Sci-Fi').values(duration=Movie.duration + 10)
        session.execute(stmt)
        session.commit()
# t30()
