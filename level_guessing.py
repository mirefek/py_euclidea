from multi_level import MultiLevel
import numpy as np
import sys
import random as rnd

class LevelGuessing:
    """
    out_size: the width and height of the sampled pictures
      The width of the sampled pictures will be 4.
      (however channel 0 is identical to channel 1, and channel 3 is empty)
    scale:
      The sample generator is imagining the level as if its size is
      out_size * scale, it is recommended to have the size
      out_size * scale at least (400, 400) because the random level generator
      is trying to keep the generated objects reasonably distant from each other
      and it could freeze in trying to achieve so, in case the surface were not
      big enough.
      Also the widths of lines and sizes of points are scaled down by scale
      in the output picture.
    level_dir: directory containing all the level packs
    levels:
      If None, it scans all the directories in level_dir starting with a number
      loading all python files in them as levels.
      Otherwise, it expects list of pairs (level_pack, level) where
        level_pack is the name of the appropriate dictionary
        level is the name of the .py file without extension.
      If 'level is None', it scans for all the levels in the level_pack.
    """
    def __init__(self, out_size = (256, 256), scale = (2,2),
                 level_dir = '.', levels = None):

        self.level_dir = level_dir

        import os
        if levels is None:
            levels = [
                (pack,None)
                for pack in os.listdir(level_dir)
                if pack[0].isdigit()
            ]
        levels_concrete = set()
        for level_pack, level in levels:
            if level is None:
                for fname in os.listdir(os.path.join(level_dir, level_pack)):
                    if fname.endswith(".py"):
                        levels_concrete.add((level_pack, fname[:-3]))
            else: levels_concrete.add((level_pack, level))
        self.labels = sorted(levels_concrete)

        #for pack, level in levels:
        #    print(pack, level)
        self.generator = MultiLevel(self.labels, out_size = out_size, scale = scale)

    def labels_num(self):
        return len(self.labels)
        
    def sample_single(self):
        label = self.generator.next_level()
        return self.generator.get_state(), label

    """
    sample(n) generates a list of size n.
    each element of the list is a pair (picture, label)
    where picture is a numpy array of size [out_size[0], out_size[1], 4]
    and label is a number from range(self.labels_num)
    """
    def sample(self, size):
        return [self.sample_single() for _ in range(size)]

if __name__ == "__main__":
    level_guessing = LevelGuessing()
    print(level_guessing.labels_num(), 'labels in total')

    pic, label = level_guessing.sample_single()
    print('current level:', label)
    print(pic[:,:,0])
    print('nonempty initial state:', (pic[:,:,0] != 0).any())
    print('constructed = initial:', (pic[:,:,1] == pic[:,:,0]).all())
    print(pic[:,:,2])
    print('nonempty goal:', (pic[:,:,2] != 0).any())
    print('empty selection:', (pic[:,:,3] == 0).all())

    print('sampling 1000 levels...')
    for _ in range(20): level_guessing.sample(50)
