import king
import points as pt
import unittest
import village

class TestKingAttack(unittest.TestCase):
    def setUp(self):
        self.level = 1
        self.V = village.createVillage(self.level)
        self.King = king.spawnKing(pt.config["hero_pos"])
        self.cannons = self.V.cannons
        self.wizard_towers = self.V.wizard_towers
        self.huts = self.V.huts
        self.walls = self.V.walls_top + self.V.walls_bottom + self.V.walls_left + self.V.walls_right + self.V.walls_topright + self.V.walls_topleft + self.V.walls_bottomright + self.V.walls_bottomleft

    def tearDown(self):
        pass

    def test_attack_cannons(self):
        for cannon in self.cannons:
            target = self.V.cannon_objs[cannon]
            self.King.alive = False
            target.health = target.max_health
            self.King.attack = target.health / 2
            self.King.attack_target(target, self.King.attack)
            self.assertEqual(target.health, target.max_health)

            self.King.alive = True
            target.health = target.max_health
            self.King.attack = target.health / 2
            self.King.attack_target(target, self.King.attack)
            self.assertEqual(target.health, target.max_health - self.King.attack)

            self.King.alive = True
            target.health = target.max_health
            self.King.attack = target.health
            self.King.attack_target(target, self.King.attack)
            self.assertEqual(target.destroyed, True)

    def test_attack_wizard_towers(self):
        for wizard_tower in self.wizard_towers:
            target = self.V.wizard_tower_objs[wizard_tower]
            self.King.alive = False
            target.health = target.max_health
            self.King.attack = target.health / 2
            self.King.attack_target(target, self.King.attack)
            self.assertEqual(target.health, target.max_health)

            self.King.alive = True
            target.health = target.max_health
            self.King.attack = target.health / 2
            self.King.attack_target(target, self.King.attack)
            self.assertEqual(target.health, target.max_health - self.King.attack)

            self.King.alive = True
            target.health = target.max_health
            self.King.attack = target.health
            self.King.attack_target(target, self.King.attack)
            self.assertEqual(target.destroyed, True)

    def test_attack_town_hall(self):
        target = self.V.town_hall_obj
        self.King.alive = False
        target.health = target.max_health
        self.King.attack = target.health / 2
        self.King.attack_target(target, self.King.attack)
        self.assertEqual(target.health, target.max_health)

        self.King.alive = True
        target.health = target.max_health
        self.King.attack = target.health / 2
        self.King.attack_target(target, self.King.attack)
        self.assertEqual(target.health, target.max_health - self.King.attack)

        self.King.alive = True
        target.health = target.max_health
        self.King.attack = target.health
        self.King.attack_target(target, self.King.attack)
        self.assertEqual(target.destroyed, True)

    def test_attack_huts(self):
        for hut in self.huts:
            target = self.V.hut_objs[hut]
            self.King.alive = False
            target.health = target.max_health
            self.King.attack = target.health / 2
            self.King.attack_target(target, self.King.attack)
            self.assertEqual(target.health, target.max_health)

            self.King.alive = True
            target.health = target.max_health
            self.King.attack = target.health / 2
            self.King.attack_target(target, self.King.attack)
            self.assertEqual(target.health, target.max_health - self.King.attack)

            self.King.alive = True
            target.health = target.max_health
            self.King.attack = target.health
            self.King.attack_target(target, self.King.attack)
            self.assertEqual(target.destroyed, True)

    def test_attack_walls(self):
        for wall in self.walls:
            target = self.V.wall_objs[wall]
            self.King.alive = False
            target.health = target.max_health
            self.King.attack = target.health / 2
            self.King.attack_target(target, self.King.attack)
            self.assertEqual(target.health, target.max_health)

            self.King.alive = True
            target.health = target.max_health
            self.King.attack = target.health / 2
            self.King.attack_target(target, self.King.attack)
            self.assertEqual(target.health, target.max_health - self.King.attack)

            self.King.alive = True
            target.health = target.max_health
            self.King.attack = target.health
            self.King.attack_target(target, self.King.attack)
            self.assertEqual(target.destroyed, True)
            self.V.wall_objs[wall] = target

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestKingAttack)
    result = unittest.TestResult()
    suite.run(result)
    f= open("output_bonus.txt",'w')
    if result.wasSuccessful():
        f.write("True")
        f.close()
        exit(0)
    else:
        f.write("False")
        f.close()
        exit(1)