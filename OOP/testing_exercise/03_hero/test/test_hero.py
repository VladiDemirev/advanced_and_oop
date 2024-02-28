from unittest import TestCase, main

from project.hero import Hero


class HeroTests(TestCase):
    username = "Hero"
    health = 10.5
    damage = 100.5
    level = 20

    def setUp(self):
        self.hero = Hero(self.username, self.level, self.health, self.damage)

    def test_initialization(self):
        self.assertEqual(self.username, self.hero.username)
        self.assertEqual(self.health, self.hero.health)
        self.assertEqual(self.damage, self.hero.damage)
        self.assertEqual(self.level, self.hero.level)

    def test_battle_hero_and_enemy_same_name_raises_exception(self):
        enemy = Hero(self.username, self.level, self.health, self.damage)
        with self.assertRaises(Exception) as ex:
            self.hero.battle(enemy)
        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_hero_energy_not_enough_raises_error(self):
        enemy = Hero("Enemy", self.level, self.health, self.damage)
        self.hero.health = 0
        with self.assertRaises(ValueError) as error:
            self.hero.battle(enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(error.exception))

        self.hero.health -= 1
        with self.assertRaises(ValueError) as error2:
            self.hero.battle(enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(error2.exception))

    def test_battle_enemy_energy_not_enough_raises_error(self):
        enemy = Hero("Enemy", self.level, 0, self.damage)
        with self.assertRaises(ValueError) as error:
            self.hero.battle(enemy)
        self.assertEqual(f"You cannot fight {enemy.username}. He needs to rest", str(error.exception))

        enemy.health -= 1
        with self.assertRaises(ValueError) as error2:
            self.hero.battle(enemy)
        self.assertEqual(f"You cannot fight {enemy.username}. He needs to rest", str(error2.exception))

    def test_battle_draw(self):
        enemy = Hero("Enemy", self.level, self.health, self.damage)
        result = self.hero.battle(enemy)
        self.assertEqual("Draw", result)
        self.assertEqual(-1999.5, self.hero.health)
        self.assertEqual(self.level, self.hero.level)
        self.assertEqual(self.damage, self.hero.damage)

    def test_battle_hero_wins(self):
        enemy = Hero("Enemy1", 1, 1, 1)
        result = self.hero.battle(enemy)
        self.assertEqual("You win", result)
        self.assertEqual(14.5, self.hero.health)
        self.assertEqual(self.level + 1, self.hero.level)
        self.assertEqual(self.damage + 5, self.hero.damage)

    def test_battle_enemy_wins(self):
        enemy = Hero("Enemy2", 100, 100, 100)
        self.hero.damage = 1
        result = self.hero.battle(enemy)
        self.assertEqual("You lose", result)
        self.assertEqual(85, enemy.health)
        self.assertEqual(101, enemy.level)
        self.assertEqual(105, enemy.damage)

    def test_str_returns_correct_string(self):
        expected_result = f"Hero {self.username}: {self.level} lvl\n" \
               f"Health: {self.health}\n" \
               f"Damage: {self.damage}\n"
        self.assertEqual(expected_result, str(self.hero))



if __name__ == "__main__":
    main()
