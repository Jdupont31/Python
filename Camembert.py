import matplotlib.pyplot as plt
from PIL import Image
import os

print("Veuillez rentré 4 chiffres et le total doit 100%. \nMerci")
i = input()

numbers = list(map(int, i.split()))

if len(numbers) != 4 or sum(numbers)!=100:
    print("Erreurs il n'y a pas 4 chiffres ou le total n'est pas 100% !")
else:
    #Desk
    userhome = os.path.expanduser('~')
    desk = userhome + "\desktop"
    print(desk)

    # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    labels = 'pates', 'chat', 'oiseau', 'chien'
    explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

    fig1, ax1 = plt.subplots()
    ax1.pie(numbers, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=130)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.


    #plt.imsave('UN.png')
    plt.savefig(desk+'\c.png')
    im = Image.open(desk+'\c.png')
    rgb_im = im.convert('RGB')
    rgb_im.save(desk+'\c.jpg')
    #os.remove(desk+'\c.png')
    plt.show()