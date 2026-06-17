# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
  - The game looked fine at first glance. It has a field to type guesses, a button to submit, a new game button, and show hint option. All good things, but after some investigation they're pretty buggy,
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
  - I first noticed that the hints being given were the opposite of what should be suggested. For example, hinting 'Go HIGHER!' when the guess needs to be lower. I also saw that there is no error message for an out of bounds value like zero. Considering all the possible ranges for this game start at one, that edge case seems like an easy thing to test for.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| Guess of 50 | Show 'Go LOWER!' hint for secret of 24 | Showed 'Go HIGHER! hint' | None
| Guess of 39 | Show 'Go HIGHER!' hint for secret of 78 | Showed 'Go LOWER! hint' | None
| Guess of 0 | Out of range error | Accepted value and showed 'Go LOWER!' hint | None
| Normal difficulty has range of 1-100 | Normal should have range of 1-50, hard should have 1-100 | The ranges are swapped for those levels | None
| Click new game button | New game starts | Nothing happens | None

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
I used Claude, integrated into my VSCODE IDE. I also Claude in a browser to check my usage so far for this project. I also needed to learn how to configure it a bit in VSCODE, so Gemini was useful for some quick helpful instructions. 

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
The AI suggested the proper ranges for values in the Normal and Hard difficulty levels. I verified the suggested fix by seeing that as the difficulty progresses, the range for possible values grows larger. I then tested the game in my local browser to verify the results.


- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
The AI suggested a very specific function name (test_guess_90_secret_42) for a generated test case, which wasn't inherently bad, it just didn't follow the pre-existing naming conventions. I went back and asked it to use more plain English to match the existing cases and the name suggestion improved (test_guess_way_too_high). When I ran the pytest command (after updating the assertion statements) the 4 test cases passed successfully.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I considered a bug fixed after about 5 manual tests. I used the dev inspect section for the higher/lower hint issue to ensure the hints were accurate for the secret number. For the difficulty range issue, I checked each category manually and multiple times on game restart. 

- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
I tried to run the pytest command with the existing test cases and all of them failed! I had to edit the assertion statement to account for the check_guess function returning a pair of strings - not just one string. After changing the equality operator to 'in' (since emojis broke the code), I was able to verify the test cases passed. 

- Did AI help you design or understand any tests? How?
Claude helped create a new test case to check the guess and get the proper hint. The test case it generated didn't specifically deal with any new edge case. However, it helped me realize that multiple test cases are valuable to verify the code is working as intended.


---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
I would say, Streamlit's "reruns" make your code run from the beginning every time a user interacts with the site. The site feels normal to interact with, but it's always going again in the background. Streamlit's session state allows us to persist some values in the st.session_state dictionary to combat the rerun wiping the board clean each interaction. 
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
  I haven't used pytest very much before so that's something I'll take away from this project! I mainly have only done manual testing but running a file of test cases (that AI can help generate) is super useful. I'd use this functionality probably more for projects than labs though.

- What is one thing you would do differently next time you work with AI on a coding task?
I would try giving more context next time I use an AI. Attaching files is great, but in order to solve bugs that have logic issues, that may be acceptable in other areas, just explaining things a bit more would improve the quality of the answers. I also would try a different model for more complex issues!

- In one or two sentences, describe how this project changed the way you think about AI generated code.
This project changed the way I look at AI generated code by forcing me to slow down. It required me to be more methodical about what exactly I wanted out of the AI. That helped me to see an increased value in the code, instead of larger scrutiny because it was a 'fast answer'.