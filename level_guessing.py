from multi_level import MultiLevel
import numpy as np
import sys
import random as rnd

class LevelGuessing:
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
        self.generator = MultiLevel(self.labels)

    def labels_num(self):
        return len(self.labels)
        
    def sample_single(self):
        label = self.generator.next_level()
        return self.generator.get_state(), label

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
