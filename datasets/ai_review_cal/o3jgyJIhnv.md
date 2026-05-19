- Decision: Reject
- Avg Score: 4.00
- Scores: 5, 5, 3, 3
Now I have a clear picture of the paper. Let me produce the final consolidated review.

---

## Summary

PADriver is a closed-loop personalized autonomous driving framework built on a Multi-modal Large Language Model (Vicuna-7B + CLIP-ViT-Large). It takes streaming BEV frames and textual prompts (system prompt, personalized mode prompt, ego state queue) and autoregressively generates scene descriptions, danger-level estimates for each candidate action, and the final action decision. The paper also introduces PAD-Highway, a benchmark based on the Highway-Env simulator comprising 250 hours of driving data (rule-based + human-collected) and a multi-perspective evaluation suite covering efficiency, safety, and comfort. The main claimed novelty is explicit danger-level modeling and prompt-based switching between three driving modes (slow/normal/fast).

---

## Strengths

1. **Explicit danger-level estimation for actions** — The paper introduces a `<DANGER_LEVEL>` token that assigns a risk score to each potential action, claims to be the first MLLM-based method to do so explicitly (Section 1), and provides ablation evidence (Table 3b) that adding this component yields performance gains. Table 3c further shows that the average danger level of the taken action differs meaningfully across the three modes (higher in fast mode), confirming the token is not spurious.

2. **Prompt-based multi-mode driving with a single model** — The same model produces measurably different driving behaviors by changing only the `<PERSONALIZE>` prompt (no retraining). Table 1 reports distinct metrics across slow/normal/fast modes (e.g., average speed ranging from 35.3 to 45.8 km/h), demonstrating that the system can accommodate multiple driving styles.

3. **Comprehensive closed-loop benchmark and metrics** — PAD-Highway provides 250 hours of data (235h rule-based + 25h human-collected) and an evaluation suite with 8 metrics covering efficiency (distance, speed, success rate), safety (safe-distance keeping rate, vehicle density), and comfort (average acceleration and jerk in x/y directions), going beyond simpler metrics like "Success Steps" used in prior Highway-Env work (Section 3.3).

4. **Systematic ablation studies** — Tables 3 and 4 present controlled experiments isolating the effects of danger level, scene descriptions, BEV images, and ego-state components (actions, coordinates, speed). The ablation in Table 4 usefully diagnoses that removing historical actions causes total failure (0 successful completions), revealing an action-shortcut issue that the paper openly discusses.

---

## Weaknesses

### Fatal

- **The paper claims state-of-the-art performance but provides no comparison against any other method in the experimental text.** The abstract states that PADriver "outperforms state-of-the-art approaches" and the contributions claim that "slow mode achieves state-of-the-art performance." Yet the entire Experiments section (Section 4) contains only ablation studies of PADriver's own components — there is no section describing what methods were compared, how they were configured, or any quantitative comparison. Tables 1 and 2 (embedded as images) are described as "Comparative analysis of strategies for different driving modes," which on its face reads as a comparison of PADriver's own three modes. Even if the tables in the original PDF contain baseline names (the parser strips images), the text provides zero description of the comparison setup, making the central claim of the paper unverifiable. **A paper whose core claim of "state-of-the-art performance" cannot be checked against the text has a fatal structural flaw.**

### Major

- **No comparison against non-MLLM baselines.** Even if MLLM-based methods are compared in the tables, the paper does not include rule-based controllers (e.g., IDM+MOBIL, which are native to Highway-Env), reinforcement learning policies (e.g., DQN, PPO), or simple imitation learning baselines. Without such comparisons, the necessity of deploying a 7B-parameter MLLM for this relatively simple driving task is not justified.

- **Evaluation is limited to a single toy simulator (Highway-Env) with no evidence of generalization.** Highway-Env is a 2D top-down simulator with schematic traffic, clean BEV perception, and a small discrete action space (LANE_LEFT, LANE_RIGHT, FASTER, SLOWER, KEEP). The paper acknowledges this only in the conclusion (Section 5, Limitation) but does not temper the abstract's or introduction's sweeping claims about "personalized autonomous driving." "State-of-the-art" on Highway-Env does not translate to meaningful claims about real-world personalized driving.

- **No variance or statistical confidence is reported.** Results are presented as single numbers (no error bars, no multiple runs with different random seeds). The evaluation uses only 30 fixed seeds; with such a small test set, run-to-run variance in training could be substantial and is unaccounted for.

### Minor

- **The "personalization" is limited to three coarse, predefined modes (slow/normal/fast) that differ primarily in target speed.** The paper does not demonstrate adaptation to individual users beyond having 20 drivers self-score into these three buckets. There is no test-time evaluation of whether the system can match a new user's specific preferences, and no user study validating that the behaviors produced are actually preferred.

- **The action-shortcut problem (Section 4, Table 4 Exp. 2) raises concerns about what the model has actually learned.** Without historical action tokens, the model achieves zero successful completions. The paper attributes this to the "keep" action dominating the dataset distribution and discusses it honestly, but it indicates that the MLLM heavily relies on copying the previous action rather than genuine scene understanding.

- **The danger-level ablation (Table 3b) shows incremental improvement but is not compared against a simpler non-LLM danger estimator** (e.g., time-to-collision or a rule-based risk metric). It is unclear whether the danger-level token adds value beyond what a cheap heuristic would provide.

- **Training hyperparameters are not reported.** The "Implementation Details" section (Section 4.1) names the model architectures (Vicuna-7B, CLIP-ViT-Large) but omits learning rate, batch size, optimizer, number of training steps, hardware, and training time. This limits reproducibility.

### Trivial

- The paper contains a few minor formatting issues (e.g., "autoaggressively" in the abstract appears to be a typo for "autoregressively"). These do not affect scientific content.

---

## Nice-to-Haves

- A user study where multiple participants drive in the simulator, then evaluate whether the model's behavior in each prompted mode matches their preferred style, would meaningfully strengthen the personalization claim.
- Comparison against a DQN or PPO policy trained on the same Highway-Env environment would clarify whether the MLLM complexity is warranted.
- Reporting results with variance across multiple training runs would improve statistical credibility.

---

## Removed Points

These points from the inputs were removed with justification:

- **"Training data contamination risk (same seed distribution for train/eval)"** — Seeds 0–30 are used for evaluation, remaining seeds for training data generation. Since different seeds produce different scene initializations, this is not a contamination issue; removed as factually incorrect.
- **"The method's novelty is thin / straightforward fine-tuning"** — This is a general opinion, not a specific, verifiable weakness. The danger-level estimation is a specific novel component; whether the reader finds it "thin" is subjective and not a concrete flaw.
- **"Baselines cannot be independently verified"** — Removed per hard rule: the instruction prohibits questioning the existence of cited items. The proper concern (which I retain in Major) is that baselines are not described in the text, not that existing baselines are questionable.
- **"Missing related works"** — Removed per hard rule: I cannot confirm existence of related works not cited.
- **"Missing appendix/proofs"** — Removed per hard rule: parser strips these; they exist in the original submission.
- **"Typos/grammar/formatting nitpicks"** — Removed per hard rule.
- **"Reproducibility concerns about undisclosed hyperparameters"** — Retained in Minor (it is a valid concern about missing training details), but the Harsh Critic's stronger phrasing ("entirely missing") is reduced.
- **Strength Finder strengths that are generic** — Strength about "two-stage training strategy" removed: this is standard practice for MLLMs (used in LLaVA, etc.) and not a distinguishing contribution. All other strengths from the Strength Finder are retained as they are specific and evidenced.

---

## Novel Insights

None beyond the paper's own contributions. The reviews surface the gap between the paper's ambitious claims ("SOTA personalized autonomous driving") and its actual evidence (ablation studies on a 2D simulator with no named baselines). The action-shortcut diagnosis in Table 4 is useful but is already discussed in the paper.

---

## Suggestions

1. **Add a dedicated comparison section** that names every baseline method, describes how it was configured, and presents quantitative results in a table visible in text (not only in images).
2. **Include non-MLLM baselines** — at minimum a rule-based controller (IDM+MOBIL) and a DQN/PPO policy on the same simulator — to justify the need for an MLLM approach.
3. **Report variance** across multiple training runs or seeded evaluations.
4. **Either substantially temper the "state-of-the-art" claims** to match what is actually demonstrated, or remove them until proper comparisons are performed.
5. **Provide full training hyperparameters** (learning rate, batch size, optimizer, scheduler, GPU hours) for reproducibility.
6. **Consider evaluating on a more realistic closed-loop simulator** (e.g., CARLA) as a follow-up; even one realistic scenario would significantly strengthen real-driving relevance.

---
