import ex1


print("Testing Creature with healing capability")

factory_healing = ex1.HealingCreatureFactory()

print(" base:")
creature = factory_healing.create_base()
print(creature.describe())
print(creature.attack())
print(creature.heal())

print(" evolved:")
creature_evolved = factory_healing.create_evolved()
print(creature_evolved.describe())
print(creature_evolved.attack())
print(creature_evolved.heal())

print()
print("Testing Creature with transform capability")

factory_transform = ex1.TransformCreatureFactory()

print(" base:")
creature_transformed = factory_transform.create_base()
print(creature_transformed.describe())
print(creature_transformed.attack())
print(creature_transformed.transform())
print(creature_transformed.attack())
print(creature_transformed.revert())
print(creature_transformed.attack())

print(" evolved:")
creature_transformed_evolved = factory_transform.create_evolved()
print(creature_transformed_evolved.describe())
print(creature_transformed_evolved.attack())
print(creature_transformed_evolved.transform())
print(creature_transformed_evolved.attack())
print(creature_transformed_evolved.revert())
print(creature_transformed_evolved.attack())
