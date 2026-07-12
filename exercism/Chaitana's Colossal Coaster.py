'''🏥 Hospital Triage System
Phòng cấp cứu nhận bệnh nhân liên tục, mỗi người có (tên, mức_độ, thời_gian_chờ):

mức_độ: 1 = nguy kịch, 2 = nặng, 3 = nhẹ
thời_gian_chờ: số phút đã chờ

Rule sắp xếp ưu tiên:

Ưu tiên mức độ thấp hơn (1 trước 2 trước 3)
Cùng mức độ thì ai chờ lâu hơn lên trước
Bệnh nhân mức 3 mà chờ >= 30 phút thì tự động nâng lên mức 2'''
def triage(patients):
      upgrade = [(x,2,z) if y ==3 and z >= 30 else (x,y,z) for x,y,z in patients]
      for x,y,z in patients: 
          if y ==3 and z >= 30:
            print(f"{x} được nâng lên mức 2 vì chờ {z} phút") 
      upgrade.sort(key=lambda x: (x[1], -x[2]))
      return upgrade

'''Làm thêm'''

def summarize(result):
    level = {"level_1": [], "level_2": [], "level_3": [], "longest_wait": ""}
    for x,y,z in result:
        level[f"level_{y}"].append(x)
    waitest_person = max(patients, key= lambda i: i[2])[0]
    level["longest_wait"] = f"{waitest_person}"
    return level
patients = [
    ("An", 3, 45),
    ("Bình", 1, 10),
    ("Chi", 2, 20),
    ("Dũng", 3, 15),
    ("Em", 2, 35),
]
print("Danh sách thứ tự bệnh nhân =", triage(patients))
print("Danh sách tóm tắt kết quả =", summarize(patients))
print("-----------------------------------")
''' Thư viện sách
Mỗi cuốn sách có (tên, thể_loại, năm, số_lượt_mượn). Implement 2 hàm:
1. filter_books(books, min_borrows) — trả về list sách có lượt mượn >= min_borrows, sort theo lượt mượn giảm dần.
2. group_by_genre(books) — trả về dict gom sách theo thể loại, mỗi thể loại chỉ chứa tên sách:'''
def filter_books(books: list, min_borrows: int) -> list:
    '''Trước hết, sắp xếp list theo thứ tự lượt mượn giảm dần, rồi mới dùng for xét điều kiện min_borrow'''
    books.sort(key= lambda i: i[3], reverse = True)
    books = [(a,b,c,d) for a,b,c,d in books if d >= min_borrows]
    return books
def group_by_genre(books):
    genre = {}
    for a,b,c,d in books:
        genre.setdefault(b, []).append(a)
    return genre
books = [
    ("Dune", "sci-fi", 1965, 120),
    ("1984", "dystopia", 1949, 95),
    ("Foundation", "sci-fi", 1951, 80),
    ("Brave New World", "dystopia", 1932, 60),
    ("Neuromancer", "sci-fi", 1984, 40),
]
print("Danh sách lượt mượn =", filter_books(books, 82))
print("Danh sách thể loại =", group_by_genre(books))