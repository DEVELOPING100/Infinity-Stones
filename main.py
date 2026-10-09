from ghost import Ghost

def main():
    print("╔══════════════════════════════════════╗")
    print("║     Infinity Stones — AI Router      ║")
    print("╚══════════════════════════════════════╝\n")
    
    ghost = Ghost()
    
    while True:
        print("Choose a task type:")
        print("  [1] Code")
        print("  [2] Creative")
        print("  [3] Analytical")
        print("  [4] General")
        print("  [q] Quit\n")
        
        choice = input("Select (1-4): ").strip()
        if choice.lower() == 'q':
            print("Goodbye!")
            break
            
        task_map = {
            "1": "code",
            "2": "creative", 
            "3": "analytical",
            "4": "general"
        }
        
        if choice not in task_map:
            print("Invalid choice. Try again.\n")
            continue
            
        task_type = task_map[choice]
        query = input(f"\nEnter your {task_type} query: ").strip()
        
        if not query:
            print("Query cannot be empty.\n")
            continue
        
        print(f"\n⚡ Routing to models...\n")
        result = ghost.route(query, task_type)
        
        print("─" * 50)
        print("🟢 GPT-4o Response:")
        print(result["openai"])
        print("\n🔵 Claude Response:")
        print(result["anthropic"])
        print("\n🔴 Gemini Response:")
        print(result["gemini"])
        print("\n✨ Ghost Merged Output:")
        print(result["merged"])
        print("─" * 50 + "\n")

if __name__ == "__main__":
    main()