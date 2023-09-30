import cv2
list_names - ["Mehul kumar maurya","Brijesh"]
for index, name ln enumerate(list_names):
    template=cv2.inread( 'Certificate Template.jpg')
    cv2.putText(template, name, (220, 585), cv2.FONT_HERSHEY_COMPLEX, 0.4, (8, 0, 255), 1, cv2.LTNE_AA)
    cv2.imrite(f'E:\Certificate PY\Generated\{name}.Jpg', template)
    print ('Proccessing Certificate {}/{}'.format (index+1, len(list_names)))
