## Summary
The paper proposes RLAD, an offline RL framework that trains an anomaly detection (AD) model (Deep SVDD or DAGMM) on offline state-action pairs and uses the resulting anomaly scores as per-sample weights in the critic and actor updates of an off-policy algorithm (SAC, BEAR). The authors claim that the resulting weighting mitigates Q-value overestimation without inducing CQL-style over-conservatism and report near-SOTA performance on D4RL MuJoCo and Adroit tasks.

## Strengths
- **Conceptually clean, modular framing**: decoupling the OOD signal from the RL objective by using a separately trained AD model is simple, requires no new regularizer, and is in principle compatible with multiple AD modules and RL backbones. The paper demonstrates this by instantiating four combinations (SAC/BEAR × SVDD/DAGMM).
- **Direct improvement over vanilla offline SAC**: the experimental setup includes vanilla offline SAC as a control, allowing a meaningful before/after comparison that isolates the contribution of the weighting mechanism (Table 1 — verifiable from the prose).
- **Two-axis evaluation**: the paper evaluates both behavior (normalized returns on D4RL MuJoCo and Adroit medium/medium-replay/medium-expert/human/cloned) and a diagnostic (Q-difference distribution analysis on halfcheetah-medium-v2 and Pendulum), showing some intent to connect mechanism to outcome.

## Weaknesses

### Fatal
None — but the major issues below collectively make the contribution unsupported as stated.

### Major
- **Heterogeneous baseline comparison protocol.** §5.3 and the captions of Tables 1–3 explicitly state "baseline values are taken from each paper." Numbers reported in different prior papers use different D4RL versions (v0/v1/v2), different episode counts, different seed counts, and different evaluation conventions. RLAD's own runs (5 seeds) are then juxtaposed against these to declare "best performance on most environments." This cannot establish state-of-the-art and is the primary support for empirical contribution (3).
- **Mechanism is misaligned with the diagnosed cause of overestimation.** §4 correctly identifies that overestimation in offline RL arises when the *bootstrapped* next action a' ~ π_φ(·|s') falls outside the data support. The critic update (Alg. 1 line 10) does weight by `weight(s', a')`, which partially targets this. However, the policy update (line 12) weights by `weight(s, a)` on (s, a) drawn from D — by construction these are in-distribution under the behavior policy, so the weights provide essentially no signal to discourage π_φ from selecting OOD actions at the next step. As written, the actor weight does not implement the claimed mitigation.
- **The "accurate Q-value" claim relies on a contaminated ground truth.** §5.1 estimates Q* using "the critic network of an SAC model trained in online setting" as a proxy. This proxy is Q^π for the online SAC's converged policy (with its own approximation error), not Q*, and is policy-dependent. Conclusions about RLAD being "closer to Q*" than CQL cannot be drawn from this comparison. Additionally, the "OOD set" used for that analysis is itself produced by an AutoEncoder + MC-Dropout module — methodologically too close to the AutoEncoder-based AD modules being validated, creating a circularity in evaluation.
- **No ablation of the weighting mechanism itself.** The paper attributes performance to "anomaly score-based weight adjustment" (contribution 2) but never ablates critic-weighting only, actor-weighting only, or the choice/shape of f(·) (1/x vs. sigmoid(−x), chosen per AD model without justification). Vanilla offline SAC is included as an outer control, but there is no controlled study isolating the design decisions of RLAD itself, so contribution (2) is unsupported.
- **Algorithm 1 contains parameter-swap errors in the core update equations.** Line 11 reads `φ ← φ − α_φ ∇_φ L_Q`, but L_Q is the Q-function loss and is parameterized by θ; similarly line 13 updates θ with ∇_θ L_π. These are the lines that constitute the actual training procedure, not a peripheral typo, and they leave the reader unable to confirm what was actually implemented.

### Minor
- **§3.2 mislabels distributional shift as "domain shift,"** a different concept in the ML literature. This is presentation but matters because the paper's motivation rests on the distinction.
- **§4.2 hand-waves the link between anomaly_score(s,a) and the behavior policy π_β(a|s).** The sentence "When the state s is fixed, this can be roughly interpreted with behavior policy" is the only justification for the central modeling assumption; no derivation or empirical validation of this relationship is offered.
- **§5.2's Pendulum-v1 + random-policy comparison is a weak demonstrator.** A 1-D state, random behavior policy regime is the easiest case for any anomaly detector and does not generalize to D4RL conclusions about Q-accuracy.
- **Reasoning for medium-expert/medium-replay performance is asserted, not analyzed.** The claim that RLAD is "robust to complex distributions" because of better multimodal performance contradicts the inductive bias of Deep SVDD (single hypersphere) and warrants explanation.

### Trivial
- Table 3 caption refers to "RLOCC" instead of "RLAD."
- "near state-of-the-art" (abstract/contributions) and "state-of-the-art in several tasks" (intro) are used interchangeably in the same paper.

## Nice-to-Haves
- A direct **behavior-cloning likelihood baseline**: weighting by an estimate of log π_β(a|s) is the natural baseline the AD-based approach should beat to justify the choice of "anomaly detection" framing over density estimation.
- A **real overestimation diagnostic**: compare on-policy Q-estimates vs. Monte Carlo rollout returns of π_φ in the simulator during training, rather than against an online SAC critic.
- A **distribution-of-weights plot across D4RL tasks**: confirm that f(·) actually spreads weights rather than collapsing to near-uniform.
- A **stronger AD module** (normalizing flows, KDE on (s,a)) to demonstrate the result is not Deep-SVDD-/DAGMM-specific.

## Removed Points
*These points are flagged to be removed, treat them with caution.*

- *Harsh critic — "Tables embedded as images that the parser captured but did not transcribe."* Parser artifact, not a paper issue; the tables exist in the submission.
- *Harsh critic — request to re-run all baselines under unified protocol.* Kept as a Major weakness on protocol grounds, but the demand to re-run every cited baseline is partially scope-creep; reporting which prior paper each number comes from, plus running a small set of in-house re-runs, is closer to standard practice. Softened accordingly.
- *Strength Finder — specific numerical claims (e.g., "-0.2 → 49.5 on halfcheetah-medium," "113.5 vs 111.0 on hopper-medium-expert").* I cannot verify these from the parsed text because the tables are embedded as images; I have therefore not relied on them in the strengths section, only the qualitative claim about beating vanilla SAC.
- *Strength Finder — "well-motivated use of AD for sample weighting."* This conflicts with the verified major weakness about the assumed link between anomaly score and π_β being asserted rather than shown, so it is dropped.
- *Strength Finder — "plug-and-play flexibility validated by multiple combinations."* Kept in attenuated form (modular framing), but the empirical validation strength is conditional on the baseline-protocol concern above.

## Novel Insights
None beyond the paper's own contributions. The idea of using an independently trained density/AD model as a soft pessimism signal is intuitive and modular, but the paper does not deliver evidence sufficient to call it a validated insight.

## Suggestions
- Re-run a small but unified set of in-house baselines (CQL, IQL, TD3+BC, and at least one ensemble/uncertainty method such as EDAC) on a single D4RL version with matched seeds and episodes; mark literature-copied numbers separately in the tables.
- Add a controlled ablation: SAC-offline vs. SAC+critic-weight-only vs. SAC+actor-weight-only vs. full RLAD on the same MuJoCo subsets.
- Replace the "online-SAC critic as Q*" diagnostic with on-policy Monte Carlo return estimates of π_φ during training.
- Fix the parameter symbols in Algorithm 1 lines 11 and 13 and clarify whether the weight applied to the actor uses (s,a) from D or (s, a~π_φ); if the former, justify why this should constrain π_φ from selecting OOD actions.
- Add an explicit empirical comparison of anomaly_score(s,a) to a behavior-cloning estimate of log π_β(a|s) on at least one task to justify the AD framing.
- Provide a small theoretical or empirical argument linking the AD-model's level sets to the support of D.

---

**Axis-by-axis assessment.** *Originality*: moderate — the high-level idea of using an AD module as a weight source is natural and uncommon, but closely related to density-/uncertainty-based pessimism. *Importance of question*: high — overestimation in offline RL is a central problem. *Are claims well supported?*: largely no — the SOTA claim rests on heterogeneous baselines, and the overestimation claim rests on a confounded ground-truth proxy. *Soundness of experiments*: weak — no ablation of the proposed weighting design, missing controlled overestimation diagnostic, and core-method-algorithm typos. *Clarity*: middling — the framework is clearly described at high level, but the central theoretical link (anomaly score ≈ behavior policy) is hand-waved and Algorithm 1 contains parameter swaps. *Value to the community*: limited in the present form; the framing is reusable but the evidence does not currently support the headline claims.

## Score and Decision
The paper poses a reasonable question and proposes a clean framework, but the empirical comparison protocol is methodologically shaky, the actor-side weighting is mechanistically misaligned with the stated diagnosis of overestimation, the Q-value mitigation claim is supported only by a confounded proxy and a low-dimensional toy, no ablation isolates the proposed weighting choices, and the training-procedure equations in Algorithm 1 contain parameter-name errors. None of these individually invalidates the paper, but collectively they leave the central claims unsupported.

MY FINAL SCORE: <pineapple>3.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>