import sqlite3
conn = sqlite3.connect('restaurantmenu.db')

c = conn.cursor()
c.execute('''
    CREATE TABLE `restaurants` (
    `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
    `name` varchar(255) NOT NULL DEFAULT '',
    PRIMARY KEY (`id`)
    )
    ''')
