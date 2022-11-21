from flask import Blueprint
from . import db
from .models import Category, Keyboard

bp = Blueprint('admin', __name__, url_prefix='/admin/')

# function to put some seed data in the database


@bp.route('/dbseed/')
def dbseed():

    gaming = Category(
        id=1,
        name="Gaming",
        description="A keyboard designed for gamers. Although there are several controllers with dials and levers for games, the W, A, S and D letter keys on the standard QWERTY keyboard are also widely used."
    )
    capactive = Category(
        id=2,
        name="Capactive",
        description="This type of keyboard provides functionality similar to a standard mechanical keyboard, but its internal structure makes depressing a key quicker and quieter."
    )
    pantograph = Category(
        id=3,
        name="Pantograph",
        description="Pantograph collector is Key type used for thin keyboard such as note PCs well. It is structure similar to membrane, but by using pantograph (axes such as X-shapes) for support structure of key, stabilize key top, and even thin keyboard of short stroke prevents wobble of key."
    )
    other = Category(
        id=4,
        name="Other",
        description="There are lot of fantastic keyboards in the world. Let's find a suitable one for you."
    )

    try:
        db.session.add(gaming)
        db.session.add(capactive)
        db.session.add(pantograph)
        db.session.add(other)
        db.session.commit()
    except:
        return 'There was an issue adding the category in dbseed function'

    keyboard1 = Keyboard(id=1,
                         name="Logicool G PRO G-PKB-002LN",
                         price=143.16,
                         brand="Logicool",
                         conective="USB",
                         description="Numeric Keyless Design: There are cases where desk space is limited depending on the competition, so this key switch has a numeric key-less design to allow the mouse to move largely. Designed for many professional players;(Linear Key Feel That You Won't Feel Like It) The GX RED Linear Switch is a key switch that feels like a bit of clamming when you press it; Detachable Cable: Detachable USB cable for carrying to competitions. Easy to store and prevent connection failure so you can focus on the big game",
                         image="gaming_logicool.jpg",
                         category_id=gaming.id)
    keyboard2 = Keyboard(id=2,
                         name="AKEEYO NiZ 2022 Upgraded Version, Capacitive-Free Contactless Computer Keyboard",
                         price=287.68,
                         brand="AKEEYO",
                         conective="wireless",
                         description="The NiZ Plum Atom 68 combines the quiet operation of a rubber dome keyboard with the reliability and tactile feel of a mechanical keyboard.;To make the keyboard stable and reliable, the latest version has trigger keys that can be switched back and forth between 2mm and 3mm.",
                         image="capactive_niz.jpg",
                         category_id=capactive.id)
    keyboard3 = Keyboard(id=3,
                         name="Sanwa Supply SKB-SL17BKN USB Slim Keyboard Pantograph",
                         price=22.66,
                         brand="Sanwa Supply",
                         conective="USB",
                         description="The two-tiered keytop structure makes it easy to distinguish the boundary between adjacent keys, facilitating touch typing and preventing typing errors.",
                         image="pantograph_sanwa.jpg",
                         category_id=pantograph.id)
    keyboard4 = Keyboard(id=4,
                         name="Cloud Nine ErgoTKL",
                         price=159.75,
                         brand="Cloud Nine",
                         conective="USB",
                         description="Split Keyboard Design – Separates Up To 6.5 Inches (16.5 cm) to help eliminate wrist and shoulder pain while you type. Keeps hands and arms properly separated and helps provide pain-free typing for 8+ hours a day.; Tented Palm Support – Includes built in side slope (7 degrees) keeping hands comfortable at their natural inward angle (no separate tenting kit required). ",
                         image="ergonomic_ning.jpg",
                         category_id=other.id)
    keyboard5 = Keyboard(id=5,
                         name="LOGICOOL Wireless Keyboard Unifying Wireless Receiver K270",
                         price=24.92,
                         brand="Logicool",
                         conective="USB",
                         description="BUS: USB ;Connection method: Wireless(2.4GHz)",
                         image="wireless_logicool.jpg",
                         category_id=other.id)
    keyboard6 = Keyboard(id=6,
                         name="Redragon K552-KR Gaming keyboard",
                         price=49.99,
                         brand="Redragon",
                         conective="Wired",
                         description="MECHANICAL GAMING KEYBOARD – Black version, 60 Percent Mechanical Keyboard with Custom Switches (Cherry MX Blue equivalent). Designed for longevity with greater durability and responsiveness. The Mechanical Keyboard offers medium resistance, clicky sound, and precise tactile feedback for ultimate typing and gaming performance. The switches are of the highest quality, tested for 50 million keystrokes",
                         image="gaming_redragon.jpg",
                         category_id=gaming.id)
    keyboard7 = Keyboard(id=7,
                         name="J JOYACCESS 2.4G Slim and Compact Wireless Keyboard",
                         price=36.99,
                         brand="J JOYACCESS",
                         conective="Wireless",
                         description="【Wireless Keyboard With Numeric Keypad】Wireless keyboard has all keys in scissor-cross low profile structure;which makes it ulra-slim(keystroke travel 2mm),responsive and less noise. And you can use the Numeric Keypad for quick typing and data entry, No troubles with typing Numeric; Stable Connection&Easy To Install】The wireless keyboard has powerful and reliable connection up to 10 m which is more stable data transmit and anti-interferance in 33 feet long range. Grey keyboard Only need a USB receiver to connect for using, No need to download drivers",
                         image="pantograph_joyaccess.jpg",
                         category_id=pantograph.id)
    keyboard8 = Keyboard(id=8,
                         name="Realforce R2 Keyboard",
                         price=496.57,
                         brand="Fujitsu",
                         conective="Bluetooth",
                         description="Topre capacitive switches provide best-in-class precision and efficiency, requiring only a gentle press to register a keystroke ;Full N-key roll over (NKRO) - Type as fast as you can! Topre real Force keyboards can keep up with any number of keystrokes and ensure you're always in control ;Contoured frame and key settings allow for smooth movement across keys, reducing hand and finger fatigue. ",
                         image="capactive_realforce.jpg",
                         category_id=capactive.id)
    keyboard9 = Keyboard(id=9,
                         name="Happy Hacking Keyboard Professional Hybrid PD-KB800W",
                         price=438.75,
                         brand="HHKB",
                         conective="Bluetooth",
                         description="Multi-platform design that supports chattering-free capacitive contactless method ideal for high-speed input, ideal key touch and long life without fatigue even for long-time use, Bluetooth connection and USB connection (Type-C). In addition, it is a keyboard that sticks to everything, such as rational key layout and three-step tilt adjustment. ;The 'capacitive contactless method' that switches without contact (without bottom) realizes deep strokes and superb key touch. A supple and comfortable touch adds the value of joy to typing. ",
                         image="capactive_hhkb.jpg",
                         category_id=capactive.id)
    keyboard10 = Keyboard(id=10,
                          name="Koolertron Programmable Split Mechanical Keyboard",
                          price=376.88,
                          brand="Koolertron",
                          conective="USB",
                          description="【89 Programmable Keys & 8 Macro Keys Based Hardware】Program all 89 keys or create 8 complex macros with the configuration software to take full command of your computer. A macro key can output 31 characters. Perfect not only for gamers, but also for so many other types of users including designers and video editors ; 【Built-in MCU】After keyboard keys be set up, it will be automatically stored in keyboard's MCU, and no need reset the keyboard even replace the computer ",
                          image="other_koolertron.jpg",
                          category_id=other.id)
    keyboard11 = Keyboard(id=11,
                          name="MIHIYIRY SK61 61 Keys Mechanical Gaming Keyboard",
                          price=69.48,
                          brand="MIHIYIRY",
                          conective="USB",
                          description="【Cherry MX & HOT SWAPPABLE】 The CHARAN SK61 60% keyboard adopts the renowned Cherry MX which are also hot-swappable for this mechanical keyboard. You can freely DIY the mechanical keyboard and easily replace it with other Cherry MX without welding problems.",
                          image="gaming_mihiyiri.jpg",
                          category_id=gaming.id)
    keyboard12 = Keyboard(id=12,
                          name="ELECOM Bluetooth keyboard iOS corresponding sliding pantograph black TK-FBP049EBK",
                          price=225.52,
                          brand="Elecom",
                          conective="Bluetooth",
                          description="no menthioned",
                          image="pantograph_elecom.jpg",
                          category_id=pantograph.id)
    keyboard13 = Keyboard(id=13,
                          name="Mini Keyboard,Rii X8 Portable 2.4GHz Mini Wireless Keyboard",
                          price=28.79,
                          brand="Rii",
                          conective="USB",
                          description=" Rii 2.4GHz Mini Wireless QWERTY keyboard connected by the included usb dongle, plug and play. Small and handheld design, innovative shape,perfect for Raspberry Pi series, Android TV Box , HTPC and PC.;Mini Wireless Keyboard with Touchpad supporting multi-touch function, mouse left and right buttons,easy to type and copy/paste,making it faster and more convenient for you to move to choose what you want. ",
                          image="other_mini.jpg",
                          category_id=other.id)

    try:
        db.session.add(keyboard1)
        db.session.add(keyboard2)
        db.session.add(keyboard3)
        db.session.add(keyboard4)
        db.session.add(keyboard5)
        db.session.add(keyboard6)
        db.session.add(keyboard7)
        db.session.add(keyboard8)
        db.session.add(keyboard9)
        db.session.add(keyboard10)
        db.session.add(keyboard11)
        db.session.add(keyboard12)
        db.session.add(keyboard13)
        db.session.commit()
    except Exception as e:
        print(str(e))
        return 'There was an issue adding a keyboard in dbseed function'

    return 'DATA LOADED'
