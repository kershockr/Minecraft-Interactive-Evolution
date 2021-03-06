import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
from nbtschematic import SchematicFile
import importlib
import tensorflow as tf


# blocckid_dict = {
# 0:["Air"],
# 1:["Stone","Granite","Polished Granite","Diorite","Polished Diorite","Andesite","Polished Andesite"],
# 2:["Grass"],
# 3:["Dirt","Coarse Dirt","Podzol"],
# 4:["Cobblestone"],
# 5:["Oak Wood Plank","Spruce Wood Plank","Birch Wood Plank","Jungle Wood Plank","Acacia Wood Plank","Dark Oak Wood Plank"],
# 6:["Oak Sapling","Spruce Sapling","Birch Sapling","Jungle Sapling","Acacia Sapling","Dark Oak Sapling"],
# 7:["Bedrock"],
# 8:["Flowing Water"],
# 9:["Still Water"],
# 10:["Flowing Lava"],
# 11:["Still Lava"],
# 12:["Sand","Red Sand"],
# 13:["Gravel"],
# 14:["Gold Ore"],
# 15:["Iron Ore"],
# 16:["Coal Ore"],
# 17:["Oak Wood","Spruce Wood","Birch Wood","Jungle Wood"],
# 18:["Oak Leaves","Spruce Leaves","Birch Leaves","Jungle Leaves"],
# 19:["Sponge","Wet Sponge"],
# 20:["Glass"],
# 21:["Lapis Lazuli Ore"],
# 22:["Lapis Lazuli Block"],
# 23:["Dispenser"],
# 24:["Sandstone","Chiseled Sandstone","Smooth Sandstone"],
# 25:["Note Block"],
# 26:["Bed"],
# 27:["Powered Rail"],
# 28:["Detector Rail"],
# 29:["Sticky Piston"],
# 30:["Cobweb"],
# 31:["Dead Shrub","Grass","Fern"],
# 32:["Dead Bush"],
# 33:["Piston"],
# 34:["Piston Head"],
# 35:["White Wool","Orange Wool","Magenta Wool","Light Blue Wool","Yellow Wool","Lime Wool","Pink Wool","Gray Wool","Light Gray Wool","Cyan Wool","Purple Wool","Blue Wool","Brown Wool","Green Wool","Red Wool","Black Wool"],
# 37:["Dandelion"],
# 38:["Poppy","Blue Orchid","Allium","Azure Bluet","Red Tulip","Orange Tulip","White Tulip","Pink Tulip","Oxeye Daisy"],
# 39:["Brown Mushroom"],
# 40:["Red Mushroom"],
# 41:["Gold Block"],
# 42:["Iron Block"],
# 43:["Double Stone Slab","Double Sandstone Slab","Double Wooden Slab","Double Cobblestone Slab","Double Brick Slab","Double Stone Brick Slab","Double Nether Brick Slab","Double Quartz Slab"],
# 44:["Stone Slab","Sandstone Slab","Wooden Slab","Cobblestone Slab","Brick Slab","Stone Brick Slab","Nether Brick Slab","Quartz Slab"],
# 45:["Bricks"],
# 46:["TNT"],
# 47:["Bookshelf"],
# 48:["Moss Stone"],
# 49:["Obsidian"],
# 50:["Torch"],
# 51:["Fire"],
# 52:["Monster Spawner"],
# 53:["Oak Wood Stairs"],
# 54:["Chest"],
# 55:["Redstone Wire"],
# 56:["Diamond Ore"],
# 57:["Diamond Block"],
# 58:["Crafting Table"],
# 59:["Wheat Crops"],
# 60:["Farmland"],
# 61:["Furnace"],
# 62:["Burning Furnace"],
# 63:["Standing Sign Block"],
# 64:["Oak Door Block"],
# 65:["Ladder"],
# 66:["Rail"],
# 67:["Cobblestone Stairs"],
# 68:["Wall"-"mounted Sign Block"],
# 69:["Lever"],
# 70:["Stone Pressure Plate"],
# 71:["Iron Door Block"],
# 72:["Wooden Pressure Plate"],
# 73:["Redstone Ore"],
# 74:["Glowing Redstone Ore"],
# 75:["Redstone Torch (off))"],
# 76:["Redstone Torch (on)"],
# 77:["Stone Button"],
# 78:["Snow"],
# 79:["Ice"],
# 80:["Snow Block"],
# 81:["Cactus"],
# 82:["Clay"],
# 83:["Sugar Canes"],
# 84:["Jukebox"],
# 85:["Oak Fence"],
# 86:["Pumpkin"],
# 87:["Netherrack"],
# 88:["Soul Sand"],
# 89:["Glowstone"],
# 90:["Nether Portal"],
# 91:["Jack o'Lantern"],
# 92:["Cake Block"],
# 93:["Redstone Repeater Block (off)"],
# 94:["Redstone Repeater Block (on)"],
# 95:["White Stained Glass","Orange Stained Glass","Magenta Stained Glass","Light Blue Stained Glass","Yellow Stained Glass","Lime Stained Glass","Pink Stained Glass","Gray Stained Glass","Light Gray Stained Glass","Cyan Stained Glass","Purple Stained Glass","Blue Stained Glass","Brown Stained Glass","Green Stained Glass","Red Stained Glass","Black Stained Glass"],
# 96:["Wooden Trapdoor"],
# 97:["Stone Monster Egg","Cobblestone Monster Egg","Stone Brick Monster Egg","Mossy Stone Brick Monster Egg","Cracked Stone Brick Monster Egg","Chiseled Stone Brick Monster Egg"],
# 98:["Stone Bricks","Mossy Stone Bricks","Cracked Stone Bricks","Chiseled Stone Bricks"],
# 99:["Brown Mushroom Block"],
# 100:["Red Mushroom Block"],
# 101:["Iron Bars"],
# 102:["Glass Pane"],
# 103:["Melon Block"],
# 104:["Pumpkin Stem"],
# 105:["Melon Stem"],
# 106:["Vines"],
# 107:["Oak Fence Gate"],
# 108:["Brick Stairs"],
# 109:["Stone Brick Stairs"],
# 110:["Mycelium"],
# 111:["Lily Pad"],
# 112:["Nether Brick"],
# 113:["Nether Brick Fence"],
# 114:["Nether Brick Stairs"],
# 115:["Nether Wart"],
# 116:["Enchantment Table"],
# 117:["Brewing Stand"],
# 118:["Cauldron"],
# 119:["End Portal"],
# 120:["End Portal Frame"],
# 121:["End Stone"],
# 122:["Dragon Egg"],
# 123:["Redstone Lamp (inactive)"],
# 124:["Redstone Lamp (active)"],
# 125:["Double Oak Wood Slab","Double Spruce Wood Slab","Double Birch Wood Slab","Double Jungle Wood Slab","Double Acacia Wood Slab","Double Dark Oak Wood Slab"],
# 126:["Oak Wood Slab","Spruce Wood Slab","Birch Wood Slab","Jungle Wood Slab","Acacia Wood Slab","Dark Oak Wood Slab"],
# 127:["Cocoa"],
# 128:["Sandstone Stairs"],
# 129:["Emerald Ore"],
# 130:["Ender Chest"],
# 131:["Tripwire Hook"],
# 132:["Tripwire"],
# 133:["Emerald Block"],
# 134:["Spruce Wood Stairs"],
# 135:["Birch Wood Stairs"],
# 136:["Jungle Wood Stairs"],
# 137:["Command Block"],
# 138:["Beacon"],
# 139:["Cobblestone Wall","Mossy Cobblestone Wall"],
# 140:["Flower Pot"],
# 141:["Carrots"],
# 142:["Potatoes"],
# 143:["Wooden Button"],
# 144:["Mob Head"],
# 145:["Anvil"],
# 146:["Trapped Chest"],
# 147:["Weighted Pressure Plate (light)"],
# 148:["Weighted Pressure Plate (heavy)"],
# 149:["Redstone Comparator (inactive)"],
# 150:["Redstone Comparator (active)"],
# 151:["Daylight Sensor"],
# 152:["Redstone Block"],
# 153:["Nether Quartz Ore"],
# 154:["Hopper"],
# 155:["Quartz Block","Chiseled Quartz Block","Pillar Quartz Block"],
# 156:["Quartz Stairs"],
# 157:["Activator Rail"],
# 158:["Dropper"],
# 159:["White Hardened Clay","Orange Hardened Clay","Magenta Hardened Clay","Light Blue Hardened Clay","Yellow Hardened Clay","Lime Hardened Clay","Pink Hardened Clay","Gray Hardened Clay","Light Gray Hardened Clay","Cyan Hardened Clay","Purple Hardened Clay","Blue Hardened Clay","Brown Hardened Clay","Green Hardened Clay","Red Hardened Clay","Black Hardened Clay"],
# 160:["White Stained Glass Pane","Orange Stained Glass Pane","Magenta Stained Glass Pane","Light Blue Stained Glass Pane","Yellow Stained Glass Pane","Lime Stained Glass Pane","Pink Stained Glass Pane","Gray Stained Glass Pane","Light Gray Stained Glass Pane","Cyan Stained Glass Pane","Purple Stained Glass Pane","Blue Stained Glass Pane","Brown Stained Glass Pane","Green Stained Glass Pane","Red Stained Glass Pane","Black Stained Glass Pane"],
# 161:["Acacia Leaves","Dark Oak Leaves"],
# 162:["Acacia Wood","Dark Oak Wood"],
# 163:["Acacia Wood Stairs"],
# 164:["Dark Oak Wood Stairs"],
# 165:["Slime Block"],
# 166:["Barrier"],
# 167:["Iron Trapdoor"],
# 168:["Prismarine","Prismarine Bricks","Dark Prismarine"],
# 169:["Sea Lantern"],
# 170:["Hay Bale"],
# 171:["White Carpet","Orange Carpet","Magenta Carpet","Light Blue Carpet","Yellow Carpet","Lime Carpet","Pink Carpet","Gray Carpet","Light Gray Carpet","Cyan Carpet","Purple Carpet","Blue Carpet","Brown Carpet","Green Carpet","Red Carpet","Black Carpet"],
# 172:["Hardened Clay"],
# 173:["Block of Coal"],
# 174:["Packed Ice"],
# 175:["Sunflower","Lilac","Double Tallgrass","Large Fern","Rose Bush","Peony"],
# 176:["Free"-"standing Banner"],
# 177:["Wall"-"mounted Banner"],
# 178:["Inverted Daylight Sensor"],
# 179:["Red Sandstone","Chiseled Red Sandstone","Smooth Red Sandstone"],
# 180:["Red Sandstone Stairs"],
# 181:["Double Red Sandstone Slab"],
# 182:["Red Sandstone Slab"],
# 183:["Spruce Fence Gate"],
# 184:["Birch Fence Gate"],
# 185:["Jungle Fence Gate"],
# 186:["Dark Oak Fence Gate"],
# 187:["Acacia Fence Gate"],
# 188:["Spruce Fence"],
# 189:["Birch Fence"],
# 190:["Jungle Fence"],
# 191:["Dark Oak Fence"],
# 192:["Acacia Fence"],
# 193:["Spruce Door Block"],
# 194:["Birch Door Block"],
# 195:["Jungle Door Block"],
# 196:["Acacia Door Block"],
# 197:["Dark Oak Door Block"],
# 198:["End Rod"],
# 199:["Chorus Plant"],
# 200:["Chorus Flower"],
# 201:["Purpur Block"],
# 202:["Purpur Pillar"],
# 203:["Purpur Stairs"],
# 204:["Purpur Double Slab"],
# 205:["Purpur Slab"],
# 206:["End Stone Bricks"],
# 207:["Beetroot Block"],
# 208:["Grass Path"],
# 209:["End Gateway"],
# 210:["Repeating Command Block"],
# 211:["Chain Command Block"],
# 212:["Frosted Ice"],
# 213:["Magma Block"],
# 214:["Nether Wart Block"],
# 215:["Red Nether Brick"],
# 216:["Bone Block"],
# 217:["Structure Void"],
# 218:["Observer"],
# 219:["White Shulker Box"],
# 220:["Orange Shulker Box"],
# 221:["Magenta Shulker Box"],
# 222:["Light Blue Shulker Box"],
# 223:["Yellow Shulker Box"],
# 224:["Lime Shulker Box"],
# 225:["Pink Shulker Box"],
# 226:["Gray Shulker Box"],
# 227:["Light Gray Shulker Box"],
# 228:["Cyan Shulker Box"],
# 229:["Purple Shulker Box"],
# 230:["Blue Shulker Box"],
# 231:["Brown Shulker Box"],
# 232:["Green Shulker Box"],
# 233:["Red Shulker Box"],
# 234:["Black Shulker Box"],
# 235:["White Glazed Terracotta"],
# 236:["Orange Glazed Terracotta"],
# 237:["Magenta Glazed Terracotta"],
# 238:["Light Blue Glazed Terracotta"],
# 239:["Yellow Glazed Terracotta"],
# 240:["Lime Glazed Terracotta"],
# 241:["Pink Glazed Terracotta"],
# 242:["Gray Glazed Terracotta"],
# 243:["Light Gray Glazed Terracotta"],
# 244:["Cyan Glazed Terracotta"],
# 245:["Purple Glazed Terracotta"],
# 246:["Blue Glazed Terracotta"],
# 247:["Brown Glazed Terracotta"],
# 248:["Green Glazed Terracotta"],
# 249:["Red Glazed Terracotta"],
# 250:["Black Glazed Terracotta"],
# 251:["White Concrete","Orange Concrete","Magenta Concrete","Light Blue Concrete","Yellow Concrete","Lime Concrete","Pink Concrete","Gray Concrete","Light Gray Concrete","Cyan Concrete","Purple Concrete","Blue Concrete","Brown Concrete","Green Concrete","Red Concrete","Black Concrete"],
# 252:["White Concrete Powder","Orange Concrete Powder","Magenta Concrete Powder","Light Blue Concrete Powder","Yellow Concrete Powder","Lime Concrete Powder","Pink Concrete Powder","Gray Concrete Powder","Light Gray Concrete Powder","Cyan Concrete Powder","Purple Concrete Powder","Blue Concrete Powder","Brown Concrete Powder","Green Concrete Powder","Red Concrete Powder","Black Concrete Powder"],
# 255:["Structure Block"],
# 256:["Iron Shovel"],
# 257:["Iron Pickaxe"],
# 258:["Iron Axe"],
# 259:["Flint and Steel"],
# 260:["Apple"],
# 261:["Bow"],
# 262:["Arrow"],
# 263:["Coal","Charcoal"],
# 264:["Diamond"],
# 265:["Iron Ingot"],
# 266:["Gold Ingot"],
# 267:["Iron Sword"],
# 268:["Wooden Sword"],
# 269:["Wooden Shovel"],
# 270:["Wooden Pickaxe"],
# 271:["Wooden Axe"],
# 272:["Stone Sword"],
# 273:["Stone Shovel"],
# 274:["Stone Pickaxe"],
# 275:["Stone Axe"],
# 276:["Diamond Sword"],
# 277:["Diamond Shovel"],
# 278:["Diamond Pickaxe"],
# 279:["Diamond Axe"],
# 280:["Stick"],
# 281:["Bowl"],
# 282:["Mushroom Stew"],
# 283:["Golden Sword"],
# 284:["Golden Shovel"],
# 285:["Golden Pickaxe"],
# 286:["Golden Axe"],
# 287:["String"],
# 288:["Feather"],
# 289:["Gunpowder"],
# 290:["Wooden Hoe"],
# 291:["Stone Hoe"],
# 292:["Iron Hoe"],
# 293:["Diamond Hoe"],
# 294:["Golden Hoe"],
# 295:["Wheat Seeds"],
# 296:["Wheat"],
# 297:["Bread"],
# 298:["Leather Helmet"],
# 299:["Leather Tunic"],
# 300:["Leather Pants"],
# 301:["Leather Boots"],
# 302:["Chainmail Helmet"],
# 303:["Chainmail Chestplate"],
# 304:["Chainmail Leggings"],
# 305:["Chainmail Boots"],
# 306:["Iron Helmet"],
# 307:["Iron Chestplate"],
# 308:["Iron Leggings"],
# 309:["Iron Boots"],
# 310:["Diamond Helmet"],
# 311:["Diamond Chestplate"],
# 312:["Diamond Leggings"],
# 313:["Diamond Boots"],
# 314:["Golden Helmet"],
# 315:["Golden Chestplate"],
# 316:["Golden Leggings"],
# 317:["Golden Boots"],
# 318:["Flint"],
# 319:["Raw Porkchop"],
# 320:["Cooked Porkchop"],
# 321:["Painting"],
# 322:["Golden Apple","Enchanted Golden Apple"],
# 323:["Sign"],
# 324:["Oak Door"],
# 325:["Bucket"],
# 326:["Water Bucket"],
# 327:["Lava Bucket"],
# 328:["Minecart"],
# 329:["Saddle"],
# 330:["Iron Door"],
# 331:["Redstone"],
# 332:["Snowball"],
# 333:["Oak Boat"],
# 334:["Leather"],
# 335:["Milk Bucket"],
# 336:["Brick"],
# 337:["Clay"],
# 338:["Sugar Canes"],
# 339:["Paper"],
# 340:["Book"],
# 341:["Slimeball"],
# 342:["Minecart with Chest"],
# 343:["Minecart with Furnace"],
# 344:["Egg"],
# 345:["Compass"],
# 346:["Fishing Rod"],
# 347:["Clock"],
# 348:["Glowstone Dust"],
# 349:["Raw Fish","Raw Salmon","Clownfish","Pufferfish"],
# 350:["Cooked Fish","Cooked Salmon"],
# 351:["Ink Sack","Rose Red","Cactus Green","Coco Beans","Lapis Lazuli","Purple Dye","Cyan Dye","Light Gray Dye","Gray Dye","Pink Dye","Lime Dye","Dandelion Yellow","Light Blue Dye","Magenta Dye","Orange Dye","Bone Meal"],
# 352:["Bone"],
# 353:["Sugar"],
# 354:["Cake"],
# 355:["Bed"],
# 356:["Redstone Repeater"],
# 357:["Cookie"],
# 358:["Map"],
# 359:["Shears"],
# 360:["Melon"],
# 361:["Pumpkin Seeds"],
# 362:["Melon Seeds"],
# 363:["Raw Beef"],
# 364:["Steak"],
# 365:["Raw Chicken"],
# 366:["Cooked Chicken"],
# 367:["Rotten Flesh"],
# 368:["Ender Pearl"],
# 369:["Blaze Rod"],
# 370:["Ghast Tear"],
# 371:["Gold Nugget"],
# 372:["Nether Wart"],
# 373:["Potion"],
# 374:["Glass Bottle"],
# 375:["Spider Eye"],
# 376:["Fermented Spider Eye"],
# 377:["Blaze Powder"],
# 378:["Magma Cream"],
# 379:["Brewing Stand"],
# 380:["Cauldron"],
# 381:["Eye of Ender"],
# 382:["Glistering Melon"],
# 383:["Spawn Elder Guardian","Spawn Wither Skeleton","Spawn Stray","Spawn Husk","Spawn Zombie Villager","Spawn Skeleton Horse","Spawn Zombie Horse","Spawn Donkey","Spawn Mule","Spawn Evoker","Spawn Vex","Spawn Vindicator","Spawn Creeper","Spawn Skeleton","Spawn Spider","Spawn Zombie","Spawn Slime","Spawn Ghast","Spawn Zombie Pigman","Spawn Enderman","Spawn Cave Spider","Spawn Silverfish","Spawn Blaze","Spawn Magma Cube","Spawn Bat","Spawn Witch","Spawn Endermite","Spawn Guardian","Spawn Shulker","Spawn Pig","Spawn Sheep","Spawn Cow","Spawn Chicken","Spawn Squid","Spawn Wolf","Spawn Mooshroom","Spawn Ocelot","Spawn Horse","Spawn Rabbit","Spawn Polar Bear","Spawn Llama","Spawn Parrot","Spawn Villager"],
# 384:["Bottle o' Enchanting"],
# 385:["Fire Charge"],
# 386:["Book and Quill"],
# 387:["Written Book"],
# 388:["Emerald"],
# 389:["Item Frame"],
# 390:["Flower Pot"],
# 391:["Carrot"],
# 392:["Potato"],
# 393:["Baked Potato"],
# 394:["Poisonous Potato"],
# 395:["Empty Map"],
# 396:["Golden Carrot"],
# 397:["Mob Head (Skeleton)","Mob Head (Wither Skeleton)","Mob Head (Zombie)","Mob Head (Human)","Mob Head (Creeper)","Mob Head (Dragon)"],
# 398:["Carrot on a Stick"],
# 399:["Nether Star"],
# 400:["Pumpkin Pie"],
# 401:["Firework Rocket"],
# 402:["Firework Star"],
# 403:["Enchanted Book"],
# 404:["Redstone Comparator"],
# 405:["Nether Brick"],
# 406:["Nether Quartz"],
# 407:["Minecart with TNT"],
# 408:["Minecart with Hopper"],
# 409:["Prismarine Shard"],
# 410:["Prismarine Crystals"],
# 411:["Raw Rabbit"],
# 412:["Cooked Rabbit"],
# 413:["Rabbit Stew"],
# 414:["Rabbit's Foot"],
# 415:["Rabbit Hide"],
# 416:["Armor Stand"],
# 417:["Iron Horse Armor"],
# 418:["Golden Horse Armor"],
# 419:["Diamond Horse Armor"],
# 420:["Lead"],
# 421:["Name Tag"],
# 422:["Minecart with Command Block"],
# 423:["Raw Mutton"],
# 424:["Cooked Mutton"],
# 425:["Banner"],
# 426:["End Crystal"],
# 427:["Spruce Door"],
# 428:["Birch Door"],
# 429:["Jungle Door"],
# 430:["Acacia Door"],
# 431:["Dark Oak Door"],
# 432:["Chorus Fruit"],
# 433:["Popped Chorus Fruit"],
# 434:["Beetroot"],
# 435:["Beetroot Seeds"],
# 436:["Beetroot Soup"],
# 437:["Dragon's Breath"],
# 438:["Splash Potion"],
# 439:["Spectral Arrow"],
# 440:["Tipped Arrow"],
# 441:["Lingering Potion"],
# 442:["Shield"],
# 443:["Elytra"],
# 444:["Spruce Boat"],
# 445:["Birch Boat"],
# 446:["Jungle Boat"],
# 447:["Acacia Boat"],
# 448:["Dark Oak Boat"],
# 449:["Totem of Undying"],
# 450:["Shulker Shell"],
# 452:["Iron Nugget"],
# 453:["Knowledge Book"],
# 2256:["13 Disc"],
# 2257:["Cat Disc"],
# 2258:["Blocks Disc"],
# 2259:["Chirp Disc"],
# 2260:["Far Disc"],
# 2261:["Mall Disc"],
# 2262:["Mellohi Disc"],
# 2263:["Stal Disc"],
# 2264:["Strad Disc"],
# 2265:["Ward Disc"],
# 2266:["11 Disc"],
# 2267:["Wait Disc"],
# }


# Takes a directory of .schem files, and converts them into a combined array of size (# samples, x, y, z), where each entry is a minecraft block name (ex: minecraft:air)

mapping_df = pd.read_csv('../compression_csv.csv')
def create_combined_blockname_data(schematic_dir):
    data_list = []
    for file in os.listdir(schematic_dir):
        if file.endswith('.schem'):
            file_path = schematic_dir + '/' + file

            # load schem file
            schem = SchematicFile.load(file_path)

            # get block data, where each value corresponds to an index in the palette dictionary
            blockdata = schem.blocks.unpack()
            blockdata = blockdata.astype(object)

            # get the palette dictionary
            palette = schem.palette

            # reverse it so that the keys are indices and the values are the block names
            reverse_palette_dict = {y: x for x, y in palette.items()}

            # replace indices with their block names
            for key, value in reverse_palette_dict.items():

                # remove unwanted data from the palette string
                block_tag = reverse_palette_dict[key]
                block_tag = block_tag.partition(":")[2]
                if "[" in block_tag:
                    block_tag = block_tag.partition('[')[0]

                # print(mapping_df[mapping_df['block tag'] == block_tag])
                blockdata[blockdata == key] = block_tag

            data_list.append(blockdata)

    # print(len(data_list))
    combined = np.asarray(data_list)
    # print(combined.shape)
    uniques, counts = np.unique(combined, return_counts=True)
    # print(uniques)
    # print(counts)

    return combined
    # np.save(schematic_dir + "/combined_blocknames.npy", combined)

def convert_to_blockid(combined_array):
    uniques = np.unique(combined_array)

    # for each unique value in our combined array, replace the block name with numerical id
    for val in uniques:

        # get block id for this value
        block_id = mapping_df[mapping_df['block tag'] == val]['compressed blockid']
        if len(block_id) > 0:
            # print(val)
            block_id = int(block_id.iloc[0])
        else:
            block_id = "NOT FOUND"
            print(val, " ", block_id)

        # replace all instances of this value with the corresponding block id
        combined_array[np.where(combined_array == val)] = block_id

    uniques, counts = np.unique(combined_array, return_counts=True)
    print(uniques)
    print(counts)
    return combined_array


def cropHouse(h):
    # argwhere will give you the coordinates of every non-zero point
    true_points = np.argwhere(h)
    # take the smallest points and use them as the top left of your crop
    top_left = true_points.min(axis=0)
    # take the largest points and use them as the bottom right of your crop
    bottom_right = true_points.max(axis=0)
    out = h[top_left[0]:bottom_right[0] + 1,  # plus 1 because slice isn't
          top_left[1]:bottom_right[1] + 1, top_left[2]:bottom_right[2] + 1]  # inclusive

    return out

def houseTrans(h, s=(16, 16, 16)):
    hts = []

    s2 = cropHouse(h)
    # print("cropped house shape: ", s2.shape)
    s2s = s2.shape
    ds = (s[0] - s2s[0], s[1] - s2s[1], s[2] - s2s[2])
    # print(ds)
    # for x in range(1):
    for x in range(s[0] - s2s[0] + 1):
        # for y in range(1):
        for y in range(s[1] - s2s[1]):
            for z in range(1):
                # for z in range(s[2]-s2s[2]+1):
                thouse = np.zeros(shape=s)
                thouse[x:x + s2s[0], y:y + s2s[1], z:z + s2s[2]] = s2.copy()
                hts.append(thouse)
    # print("len of hts: ", len(hts))
    return hts

def augment(combined):
    HOUSE_DATASET = []
    HOUSE_DATASET_BIN = []
    DOUBLE_HOUSES = []
    DOUBLE_MOVE_HOUSES = []
    TRANS_HOUSES = []
    TRANS_HOUSES_PRE = []
    TRANS_DOUBLE_HOUSES = []

    # house_combined = np.load('../ingame house schematics/combined_ingame_onehot.npy')
    blocks = []
    for h in combined:
        print("h shape ", h.shape)
        # houses look rotated... just rotate them back
        h = np.rot90(h, axes=(0, 2))

        # remove bottom layer (got the ground as well) - i can't believe i got it right on the first try...
        h = h[3:, 3:, 1:-2]
        HOUSE_DATASET.append(h)

        # # binary
        # idx = np.nonzero(h)
        # hb = np.zeros(shape=h.shape)
        # for i in range(len(idx[0])):
        #     a, b, c = idx
        #     hb[a[i]][b[i]][c[i]] = 1
        # HOUSE_DATASET_BIN.append(hb)

        # crop and translate
        # tds = []
        # for di in HOUSE_DATASET_BIN:
        tds = houseTrans(h, (16, 16, 16))
        # print(len(tds))
        # TRANS_DOUBLE_HOUSES += random.choices(tds,k=20)
        # TRANS_HOUSES_PRE += tds

        # rotated
        for haus in tds:
            TRANS_HOUSES.append(haus)
            TRANS_HOUSES.append(np.rot90(haus, axes=(0, 1)))
            TRANS_HOUSES.append(np.rot90(haus, axes=(1, 0)))
            TRANS_HOUSES.append(np.rot90(np.rot90(haus, axes=(1, 0)), axes=(1, 0)))

        # doubled binary
        # h2 = hb
        # dh = np.zeros(shape=(32,32,32))
        # m = [(0,0,0),(1,0,0),(0,1,0),(0,0,1),(1,1,0),(0,1,1),(1,0,1),(1,1,1)]
        # for x in range(16):
        #     for y in range(16):
        #         for z in range(16):
        #             v = h2[x][y][z]
        #             if v == 0:
        #                 continue
        #             for mi in m:
        #                 dh[x*2+mi[0]][y*2+mi[1]][z*2+mi[2]] = v
        # DOUBLE_HOUSES.append(dh)

        # doubled binary and rotated
        # hi = np.copy(dh)
        # DOUBLE_MOVE_HOUSES.append(hi)
        # DOUBLE_MOVE_HOUSES.append(np.rot90(hi,axes=(0,1)))
        # DOUBLE_MOVE_HOUSES.append(np.rot90(hi,axes=(1,0)))
        # DOUBLE_MOVE_HOUSES.append(np.rot90(np.rot90(hi,axes=(1,0)),axes=(1,0)))

    HOUSE_DATASET = np.array(HOUSE_DATASET)
    HOUSE_DATASET_BIN = np.array(HOUSE_DATASET_BIN)
    DOUBLE_HOUSES = np.array(DOUBLE_HOUSES)
    DOUBLE_MOVE_HOUSES = np.array(DOUBLE_MOVE_HOUSES)
    TRANS_DOUBLE_HOUSES = np.array(TRANS_DOUBLE_HOUSES)
    TRANS_HOUSES = np.array(TRANS_HOUSES)

    print("\n \n Length of transormed houses: ", len(TRANS_HOUSES), "\n \n")
    return TRANS_HOUSES

combined = create_combined_blockname_data('../ingame house schematics')
converted = convert_to_blockid(combined)
print(converted.shape)
augmented = augment(converted)
print(augmented.shape)
onehot = tf.one_hot(augmented, 11, dtype=tf.int8).numpy()
print(onehot.shape)
np.save("../ingame house schematics/combined_ingame_onehot_augmented.npy", onehot)
# print(mapping_df)
