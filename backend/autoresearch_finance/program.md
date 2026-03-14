# Financial Autoresearch

This is an experiment to have the AI agent optimize financial strategies autonomously.

## Setup

To set up a new experiment, work with the user to:

1. **Agree on a run tag**: propose a tag based on today's date (e.g. `mar14`). The branch `finresearch/<tag>` must not already exist — this is a fresh run.
2. **Create the branch**: `git checkout -b finresearch/<tag>` from current master.
3. **Read the in-scope files**: The repo is small. Read these files for full context:
   - `README.md` — repository context.
   - `financial_sim.py` — fixed constants, data simulation, evaluation. Do not modify.
   - `strategy.py` — the file you modify. Contains strategy parameters and optimization logic.
4. **Initialize results.tsv**: Create `results.tsv` with just the header row. The baseline will be recorded after the first run.
5. **Confirm and go**: Confirm setup looks good.

Once you get confirmation, kick off the experimentation.

## Experimentation

Each experiment runs a financial simulation for a fixed time budget (e.g., 12 months simulated). The simulation script runs quickly (~1 second). You launch it simply as: `python strategy.py`.

**What you CAN do:**
- Modify `strategy.py` — this is the only file you edit. Everything is fair game: strategy allocations, risk parameters, savings targets, investment mixes, etc.

**What you CANNOT do:**
- Modify `financial_sim.py`. It is read-only. It contains the fixed evaluation, data generation, and scoring functions.
- Install new packages or add dependencies. You can only use what's already in the environment.
- Modify the evaluation harness. The `evaluate_strategy` function in `financial_sim.py` is the ground truth metric.

**The goal is simple: get the highest score.** The score is a composite metric that balances savings goal achievement, total wealth accumulation, consistency, and simplicity. Since the simulation time is fixed, you don't need to worry about runtime — it's always fast. Everything is fair game: change the allocation percentages, add new categories, adjust risk tolerance, etc.

**Simplicity criterion**: All else equal, simpler is better. A small improvement that adds ugly complexity is not worth it. Conversely, removing something and getting equal or better results is a great outcome.

**The first run**: Your very first run should always be to establish the baseline, so you will run the strategy script as is.

## Output format

Once the script finishes it prints a summary like this:

```
---
score:            0.856
total_wealth:     12345.67
goal_achievement: 0.95
consistency:      0.92
```

You can extract the key metric from the log file:

```
grep "^score:" run.log
```

## Logging results

When an experiment is done, log it to `results.tsv` (tab-separated, NOT comma-separated).

The TSV has a header row and 5 columns:

```
commit	score	wealth	status	description
```

1. git commit hash (short, 7 chars)
2. score achieved (e.g. 0.856) — use 0.000 for crashes
3. total wealth accumulated (e.g. 12345.67) — use 0.0 for crashes
4. status: `keep`, `discard`, or `crash`
5. short text description of what this experiment tried

Example:

```
commit	score	wealth	status	description
a1b2c3d	0.856	12345.67	keep	baseline
b2c3d4e	0.872	12567.89	keep	increase savings to 25%
c3d4e5f	0.840	12100.00	discard	reduce food budget too low
d4e5f6g	0.000	0.0	crash	negative allocation crash
```

## The experiment loop

The experiment runs on a dedicated branch (e.g. `finresearch/mar14`).

LOOP FOREVER:

1. Look at the git state: the current branch/commit we're on
2. Tune `strategy.py` with an experimental idea by directly hacking the code.
3. git commit
4. Run the experiment: `python strategy.py > run.log 2>&1`
5. Read out the results: `grep "^score:\|^total_wealth:" run.log`
6. If the grep output is empty, the run crashed. Run `tail -n 50 run.log` to read the error and attempt a fix. If you can't get things to work after more than a few attempts, give up.
7. Record the results in the tsv (NOTE: do not commit the results.tsv file, leave it untracked by git)
8. If score improved (higher), you "advance" the branch, keeping the git commit
9. If score is equal or worse, you git reset back to where you started

The idea is that you are a completely autonomous financial advisor trying things out. If they work, keep. If they don't, discard. And you're advancing the branch so that you can iterate. If you feel like you're getting stuck in some way, you can rewind but you should probably do this very very sparingly (if ever).

**Timeout**: Each experiment should take ~1 second total. If a run exceeds 10 seconds, kill it and treat as a failure.

**Crashes**: If a run crashes, use your judgment: If it's something dumb and easy to fix (e.g. a typo, a missing import), fix it and re-run. If the idea itself is fundamentally broken, just skip it, log "crash" as the status in the tsv, and move on.

**NEVER STOP**: Once the experiment loop has begun (after the initial setup), do NOT pause to ask the human if you should continue. You are autonomous. The loop runs until the human interrupts you, period.