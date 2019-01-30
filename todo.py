import json
import sys

def loadList():
    try:
        f = open('todos', 'r')
        items = json.load(f)
    except FileNotFoundError:
        f = open('todos', 'w')
        f.close()
        items = []
    return items


def addItem(itemList):
    item = ['[ ]']
    item.append(input('Add an item: '))
    itemList.append(item)
    print('Item added.')


def markItem(itemList):
    try:
        k = int(input('Which one you want to mark as completed: '))
        itemList[k-1][0] = '[X]'
        print(itemList[k-1][1]+' is completed')
    except IndexError:
        print('Task does not exist')
    except ValueError:
        pass


def archive(itemList):
    for i in itemList:
        if i[0] == '[X]':
            n = itemList.index(i)
            del itemList[n]
    print('All completed tasks got deleted.')


def printItems(itemList):
    print('You saved the following to-do items:')
    for i in range(len(itemList)):
        item = itemList[i]
        print('   ' + str(i + 1) + ". " + item[0] + " " + item[1])


def saveItems(itemList):
    with open('todos','w') as f:
        json.dump(itemList, f)
    f.closed
    

def main():
    items = loadList()

    k = input('Please specify a command [list, add, mark, archive]: ')
    if k == 'add':
        addItem(items)
        saveItems(items)
    if k == 'list':
        printItems(items)
    if k == 'mark':
        markItem(items)
        saveItems(items)
    if k == 'archive':
        archive(items)
        saveItems(items)


main()