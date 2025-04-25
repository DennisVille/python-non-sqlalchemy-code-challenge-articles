class Article:
    all = []
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        if isinstance(title, str) and 51 > len(title) > 4:
            self._title = title
        else:
            raise TypeError('title must be a string btwn 5 and 50 characters')
        Article.all.append(self)

    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, author):
        if isinstance(author, Author):
            self._author = author
        else:
            raise TypeError('author must be of Author type')
        
    @property
    def magazine(self):
        return self._magazine
    
    @magazine.setter
    def magazine(self, mag):
        if isinstance(mag, Magazine):
            self._magazine = mag
        else:
            raise TypeError('magazine must be of Magazine type')
        
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, tittle):
        raise Exception('title attribute cannot be changed')
        
class Author:

    all = []

    def __init__(self, name):
        if isinstance(name, str) and len(name) > 0:
            self._name = name
        else:
            raise TypeError('name must be a string')
        Author.all.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        raise AttributeError('name attribute cannot be changed')

    def articles(self):
        return [l for l in Article.all if l.author == self]

    def magazines(self):
        mag_list = [m.magazine for m in Article.all if m.author == self]
        mag_unique = []
        for m in mag_list:
            if m not in mag_unique:
                mag_unique.append(m)
        return mag_unique

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        mag_all = [m.magazine.category for m in Article.all if m.author == self]
        mag_unique = []
        for m in mag_all:
            if m not in mag_unique:
                mag_unique.append(m)
        return None if len(mag_unique) == 0 else mag_unique

class Magazine:
    all = []

    def __init__(self, name, category):
        self.name = name
        self.category = category
        Magazine.all.append(self)

    @property
    def name(self):
        return self._name 
    
    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str):
            if 17 > len(new_name) >1:
                self._name = new_name
            else:
                raise Exception ('name must be between 2 and 16 characters')
        else:
            raise TypeError('name must be a string')
        
    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, category):
        if isinstance(category, str) and len(category) > 0:
            self._category = category
        else:
            raise TypeError('category must be a string')

    def articles(self):
        return [l for l in Article.all if l.magazine == self]

    def contributors(self):
        mag_contributors = [l.author for l in Article.all if l.magazine == self]
        mag_unique = []
        for m in mag_contributors:
            if m not in mag_unique:
                mag_unique.append(m)
        return mag_unique

    def article_titles(self):
        mag_titles = [a.title for a in Article.all if a.magazine == self]
        return None if len(mag_titles) == 0 else mag_titles

    def contributing_authors(self):
        return_list = []
        all_authors = self.contributors()
        all_articles = self.articles()
        for author in all_authors:
            count = 0
            for article in all_articles:
                if author == article.author:  
                    count += 1
            if count > 2:
                return_list.append(author)
        return None if len(return_list) == 0 else return_list
    
    @classmethod
    def top_publisher(cls):
        all_mags = Magazine.all
        all_articles = Article.all
        return_list = []
        if len(all_articles) == 0:
            return None
        for mag in all_mags:
            count = sum(1 for article in all_articles if article.magazine == mag)
            return_list.append((mag, count))

        if not return_list:
            return None

        top = max(return_list, key=lambda x: x[1])
        return None if top[1] == 1 else top[0]