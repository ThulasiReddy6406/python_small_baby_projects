print("🏴‍☠️ Welcome to My World! 🏝️")
print("Your mission is to find the treasure! 💰")

# Step 1: Choosing a direction
direction = input("Enter direction (Left/Right): ").lower()

if direction == "left":
    print("✅ Success! You are moving to the 2nd step.")
    
    # Step 2: Swim or Wait
    next_step = input("Do you want to Swim or Wait? ").lower()
    
    if next_step == "wait":
        print("✅ Success! You enter the 3rd step.")
        
        # Step 3: Choosing a door
        last_door = input("Enter a door (Red / Blue / Yellow): ").lower()
        
        if last_door == "yellow":
            print("🎉 Congratulations! You found the treasure! 🏆💰")
        else:
            print("❌ You entered the wrong door. Game over! ☠️")
    else:
        print("❌ Oh no! You got attacked by a sea monster. Game over! ☠️")
else:
    print("❌ You fell into a trap. Game over! ☠️")
