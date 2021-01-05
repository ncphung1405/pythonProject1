list2  = [({ 'name' : 'Peter' , 'age' : 2 }, { 'name' : 'John' , 'age' : 21 }),
         ({ 'name' : 'Mary' , 'age' : 2 }, { 'name' : 'Trandanpro' , 'age' : 21 }),
         ({ 'name' : 'Nam' , 'age' : 2 }, { 'name' : 'Hung' , 'age' : 21 }),
         ({ 'name' : 'Mai' , 'age' : 2 }, { 'name' : 'Loan' , 'age' : 21 })]
cho  chỉ mục , ( x , y ) trong  liệt kê ( list2 ):
    #khi phân tích ra thì x, y là các dictionary
    for i in x: #i chạy trong x nhận các giá trị lần lượt là: 'name', 'age'
        print ( x [ i ], end = '' )
    print ( '' )
    for i in y: #i chạy trong y nhận các giá trị lần lượt là: 'name', 'age'
        print ( y [ i ], end = '' )
    print ( '' )
'''khi chạy 2 vòng for như vậy thấy khá mất thời gian
liệu có cách nào gộp 2 dòng for na ná nhau đó lại với nhau?'''