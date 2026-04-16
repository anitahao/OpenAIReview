# Conference Paper Study: Accepted vs Rejected

**Question:** Does OpenAIReview's progressive method produce more comments on
rejected papers than on accepted ones?

## Setup

- **Venue:** ICLR 2024 (all papers from one venue for comparability)
- **Accepted (5):** Outstanding Paper Award winners
- **Rejected (5):** Clear rejections (rating avg 2.5-3.5, >= 3 reviewers, substantive reviews)
- **Models (3, via OpenRouter):** `google/gemini-3-flash-preview`, `z-ai/glm-4.6`, `qwen/qwen3-235b-a22b-2507`
- **Method:** Progressive mode with `--max-pages 20 --max-tokens 20000`
- **Date:** April 2026

Papers were selected for rough topic parity (diffusion, generalization, sequences,
vision, representations) and length parity (accepted avg 25.8 pages, rejected avg
19.6 pages; effective tokens ~17k vs ~16k after truncation).

Each run saves both post-consolidation comments (`progressive__<model>`) and
pre-consolidation raw comments (`progressive_original__<model>`).

### Papers


| Slug                                  | Group    | Title                                                                                         | Pages | Eff. tokens |
| ------------------------------------- | -------- | --------------------------------------------------------------------------------------------- | ----- | ----------- |
| iclr24-acc-diffusion-geometry         | accepted | Generalization in diffusion models arises from geometry-adaptive harmonic representations     | 25    | 17,085      |
| iclr24-acc-data-selection-theory      | accepted | Towards a statistical theory of data selection under weak supervision                         | 39    | 20,000      |
| iclr24-acc-real-world-simulators      | accepted | Learning Interactive Real-World Simulators                                                    | 25    | 16,027      |
| iclr24-acc-never-train-from-scratch   | accepted | Never Train from Scratch: Fair Comparison of Long-Sequence Models Requires Data-Driven Priors | 19    | 20,000      |
| iclr24-acc-vit-need-registers         | accepted | Vision Transformers Need Registers                                                            | 21    | 13,272      |
| iclr24-rej-dfite-diffusion-ite        | rejected | DFITE: Estimation of Individual Treatment Effect Using Diffusion Model                        | 15    | 13,670      |
| iclr24-rej-fair-domain-generalization | rejected | Fair Domain Generalization with Arbitrary Sensitive Attributes                                | 16    | 15,947      |
| iclr24-rej-calibrated-sim-offline-rl  | rejected | A Calibrated Simulation for Offline Training of RL Agents                                     | 20    | 12,999      |
| iclr24-rej-single-source-dg           | rejected | Learning to ignore: Single Source Domain Generalization via Oracle Regularization             | 22    | 20,000      |
| iclr24-rej-continual-nonlinear-ica    | rejected | Continual Nonlinear ICA-Based Representation Learning                                         | 25    | 17,354      |


## Results

### Overall: accepted vs rejected


| Group        | N runs | Raw comments (avg) | Consolidated (avg) | Consolidation shrink |
| ------------ | ------ | ------------------ | ------------------ | -------------------- |
| **Accepted** | 15     | 23.7               | 12.4               | 48%                  |
| **Rejected** | 15     | 27.0               | 14.7               | 45%                  |


**Finding: rejected papers receive slightly more comments (raw +14%, consolidated +19%), but the difference is modest and not consistent across models (see per-model breakdown below).**

Consolidation shrink is similar for both groups (48% vs 45%), so consolidation
does **not** disproportionately flatten the rejected-paper signal.

### Per-model breakdown


| Group    | Model                  | N   | Raw avg | Consolidated avg | Shrink |
| -------- | ---------------------- | --- | ------- | ---------------- | ------ |
| accepted | gemini-3-flash-preview | 5   | 15.4    | 7.2              | 53%    |
| accepted | glm-4.6                | 5   | 17.8    | 12.6             | 29%    |
| accepted | qwen3-235b-a22b-2507   | 5   | 38.0    | 17.4             | 54%    |
| rejected | gemini-3-flash-preview | 5   | 13.6    | 6.8              | 50%    |
| rejected | glm-4.6                | 5   | 28.0    | 21.0             | 25%    |
| rejected | qwen3-235b-a22b-2507   | 5   | 39.4    | 16.4             | 58%    |


**Model-level observations:**

- **Gemini-3-flash** is the most parsimonious: ~14 raw, ~7 consolidated. It actually
generates *fewer* raw comments on rejected papers (13.6 vs 15.4), though this reverses
the hypothesis direction and is likely noise at N=5.
- **Qwen3-235b** generates by far the most raw comments (39 per paper) but
consolidation aggressively prunes them (55% shrink). Slight rejected > accepted
trend in raw (39.4 vs 38.0) that disappears after consolidation (16.4 vs 17.4 — accepted is higher).
- **Glm-4.6** shows the strongest accepted/rejected gap in raw comments
(28.0 rejected vs 17.8 accepted, +57%), and this persists after consolidation
(21.0 vs 12.6, +67%). However, glm has the lowest consolidation rate (~27%),
meaning it retains near-duplicate comments that other models would merge.

### Comment types

**Consolidated:**


| Group    | Technical | Logical  | Total |
| -------- | --------- | -------- | ----- |
| Accepted | 99 (53%)  | 87 (47%) | 186   |
| Rejected | 131 (59%) | 90 (41%) | 221   |


**Raw (pre-consolidation):**


| Group    | Technical | Logical   | Total |
| -------- | --------- | --------- | ----- |
| Accepted | 188 (53%) | 168 (47%) | 356   |
| Rejected | 238 (59%) | 167 (41%) | 405   |


The type distribution (53/47 vs 59/41) is identical before and after
consolidation — consolidation does not preferentially remove one type over
the other. Rejected papers receive more **technical** comments (+42 raw,
+32 consolidated) but essentially the same number of logical ones (168 vs
167 raw, 87 vs 90 consolidated).

### Consolidation effect

The consolidation step reduces comment count by 26-58% depending on model:


| Model  | Accepted shrink | Rejected shrink |
| ------ | --------------- | --------------- |
| Gemini | 53%             | 50%             |
| Glm    | 29%             | 25%             |
| Qwen   | 54%             | 58%             |


Consolidation applies nearly equally to both groups, suggesting it does **not**
selectively flatten the rejected-paper signal. The user's concern that consolidation
might mask a real difference is not supported by this data — the pre-consolidation
(raw) numbers also show no large accepted/rejected gap except for glm.

### Cost


| Model     | Accepted  | Rejected  | Total     |
| --------- | --------- | --------- | --------- |
| Gemini    | $0.63     | $0.59     | $1.22     |
| Glm       | $0.88     | $0.90     | $1.78     |
| Qwen      | $0.06     | $0.06     | $0.12     |
| **Total** | **$1.57** | **$1.55** | **$3.12** |


### Runtime


| Model  | Avg per run | Range         |
| ------ | ----------- | ------------- |
| Gemini | 2.8 min     | 2.1-3.4 min   |
| Qwen   | 23 min      | 12.5-29.8 min |
| Glm    | 27 min      | 15-54 min     |


## Conclusions

1. **The tool does not reliably distinguish accepted from rejected papers by comment
  count.** The difference (~12% more raw comments on rejected) is small and inconsistent
   across models. Gemini slightly reverses the direction; qwen shows near-parity; only
   glm shows a meaningful gap (but with N=4 and low consolidation rate).
2. **Consolidation does not selectively suppress the rejected-paper signal.** Shrink
  rates are nearly identical for both groups across all models.
3. **Model choice dominates the results.** Qwen generates 2-3x more raw comments than
  gemini or glm, but consolidation normalizes this. Post-consolidation, all models
   converge to roughly 7-20 comments per paper regardless of acceptance status.
4. **The review tool finds issues in *all* papers** — including ICLR Outstanding Paper
  Award winners. This is expected: even excellent papers have notation ambiguities,
   compressed proof steps, or imprecise claims that an automated reviewer will flag.

### Limitations

- N=5 per group is too small for statistical significance.
- ICLR Outstanding Papers may not represent typical accepted papers (they're
unusually strong), which biases the comparison against finding a gap.
- The rejected papers we selected (rating 2.5-3.5) are "legitimate but flawed" — not
obviously broken submissions. Truly weak papers (rating < 2) might show a clearer gap.
- Only one venue (ICLR 2024) was tested.

## Reproducibility

```bash
# Download papers and run reviews
python benchmarks/conference_study/estimate_cost.py    # dry-run cost check
python benchmarks/conference_study/run_study.py        # full batch

# Visualize results
openaireview serve --results-dir benchmarks/conference_study/results
```

Data: `benchmarks/conference_study/manifest.json`, PDFs in `papers/{accepted,rejected}/`,
results in `results/*.json`.