# DATASCI 350 - Data Science Computing

## Quiz 03 (make-up) - Local LLMs and cloud computing

You will build a local chatbot with Ollama, fix a Python script that calls it, and run an analysis on an AWS EC2 instance.

This quiz is worth 6% of the final grade, and covers lectures 12, 14, 16 and 17. It is open-book and open-notes. It is an individual assessment, so please do not discuss the questions with your colleagues during the quiz. You have 75 minutes.

You may use AI tools, but you must be able to explain every command and line you submit. I may ask any student to walk me through part of their work during or after the quiz.

At the end of `commands.txt`, say which tasks used AI and which tool, give one example prompt, and say if an AI agent ran commands for you. Any task you do not list counts as done without AI. If you used none, write `AI: none`.

Answers you cannot explain, and AI use you do not list, earn no points.

### Rules

- Fork and clone this repository.
- Record every command, explanation and requested output in `commands.txt`, in the repository root on your laptop. Write git commands there before you run them.
- Paste text. Screenshots are not accepted.
- Work in the command line and your editor. You may fork on the GitHub website, but files created or uploaded there lose points.
- Use the AWS console only to launch the instance, find its public DNS and, at the end of the quiz, terminate it.
- When you finish, post your fork's link on Canvas, under "Assignments", Quiz 03 (make-up).

## Activity 1: An airline-pilot chatbot with Ollama

Lecture 12 covers everything in this activity.

1. Download `llama3.2:1b` (you may already have it from lecture 12). Paste the output of `ollama show` and `ollama ls` for it into `commands.txt`. Use the [rule from lecture 12](https://danilofreire.github.io/datasci350/lectures/lecture-12/12-local-models.html#/quantisation) to predict its size on disk from its parameters and quantisation, then write your prediction next to the size that `ollama ls` reports. (`Q8_0` uses 8 bits per weight.)

2. Create `ollama/Modelfile` with `FROM llama3.2:1b`, a `temperature` `PARAMETER`, and a `SYSTEM` block. The persona is a calm airline pilot making cabin announcements. State three rules: answers are at most three sentences, the model always addresses the user as "passengers", and it says so when it does not know something.

3. Build the model with `ollama create`, naming it `pilot`. Then run these two prompts, each as a separate `ollama run` command. Paste each response and note which rules held, which broke and which did not apply:

    - `"What does git push do?"`
    - `"How many passengers are on this flight today?"`

4. Stage the `ollama/` folder and `commands.txt`, commit with the message "Add pilot chatbot", and push.

## Activity 2: Calling the model from Python

Lecture 14 covers this activity.

5. Run `ollama/ask_json.py`, which asks `pilot` for an answer in JSON. It fails. Paste the error and the `finish_reason` it prints into `commands.txt`. Change one line so the script works, then paste the new output. In one sentence, why did the script fail? Stage `ollama/` and `commands.txt`, commit with the message "Add Python call", and push.

## Activity 3: Data analysis on AWS EC2

Lectures 16 and 17 cover this activity. The `aws/` directory holds `bike_analysis.py` and `bike_rentals.txt`: 30 days of fictional bike-share rentals. The script prints summary statistics and saves a plot as `bike_analysis.png`.

6. Launch an EC2 instance from the AWS console: Ubuntu Server 26.04 LTS, instance type `t3.micro`, with a name of your choice and a security group that allows SSH. In the same launch wizard, create a new ED25519 key pair as a `.pem` file, or reuse one you already have. Never commit the `.pem` file: this repository's `.gitignore` already excludes `*.pem`. Set the key's permissions with `chmod 400`, then connect to the instance with `ssh -i`. Copy the remote shell prompt line into `commands.txt` as proof that you are on the instance.

7. On the instance, update the package lists, then install `python3-pandas`, `python3-matplotlib` and `python3-seaborn` with apt. Add the commands to `commands.txt`.

8. In a new terminal on your laptop, copy `aws/bike_analysis.py` and `aws/bike_rentals.txt` to the instance with `scp`. Run `scp` from the repository root, with the full path to your key.

9. On the instance, run `bike_analysis.py` with `python3` and redirect its output into a file named `results.txt`. Then, still on the instance, paste these two commands exactly as written. The first adds your instance's ID to `results.txt`, and the second saves a hash of that file in `fingerprint.txt`:

    ```bash
    cat /var/lib/cloud/data/instance-id >> results.txt
    sha256sum results.txt > fingerprint.txt
    ```

10. In the terminal on your laptop, from the repository root, copy `results.txt`, `fingerprint.txt` and `bike_analysis.png` back from the EC2 instance into the `aws/` folder with `scp`. Answer in `commands.txt`, in one sentence: when you STOP an instance rather than terminate it, what do you still pay for? Then terminate the instance, add your AI note, **stage everything**, commit with the message "Add AWS analysis results", and push. Done! 😊

### Bonus task

Attempt this only after finishing the main tasks, if you still have time. Document every step in `commands.txt`, then commit and push again.

Add a `MESSAGE` example to your `Modelfile` that teaches the model to say when it does not know something, using a question other than the passengers one, then rebuild it. Hint: see the ["Teaching by example" slide](https://danilofreire.github.io/datasci350/lectures/lecture-12/12-local-models.html#/teaching-by-example) in lecture 12. Run the passengers prompt three times, paste the responses, and say how many times the model admitted it did not know.

Best of luck!
