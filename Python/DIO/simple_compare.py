register = "046.345.345-94"
blocked_register = "039.039.093-23"

# Simple attribuation compare
is_blocked = register != blocked_register

print(f" The register {register} is blocked?")
print(is_blocked)