## Summary
SpookyBench is a 451-video benchmark where all content (text, object shapes, dynamic scenes) is encoded exclusively through opposing motion patterns in binary noise — individual frames appear as random noise, but the content becomes visible via the human visual system's motion-defined form perception. The central empirical finding is stark: 27 diverse Video-VLMs (open- and closed-source, ranging from 2B to 78B parameters) all achieve exactly 0% accuracy on tasks where human participants achieve 98%. Fine-tuning directly on the benchmark distribution does not overcome this failure, supporting the paper's claim of an architectural limitation.

---

## Strengths

1. **Unambiguous, universal zero-accuracy across 27 diverse models:** Table 1 shows that every tested VLM — from 2B-parameter open-source models to 72B closed-source systems like GPT-4o and Gemini 2.0 Flash, including temporal specialists like TimeChat and InternVideo2.5 — achieves exactly 0% under both direct and chain-of-thought prompting. The uniformity of failure across such diversity of architectures and scales is a substantive empirical result, not a marginal gap.

2. **Fine-tuning experiment provides strong architectural evidence:** Section 4.4 reports that after 10 epochs of targeted fine-tuning on 400 SpookyBench videos, InternVL2.5-8B and Qwen2-VL-7B still achieve 0% on the held-out test set. The paper notes "fine-tuned models produced outputs that mimicked training examples without correctly identifying test patterns." This eliminates out-of-distribution data as an explanation and places the failure at the level of architecture.

3. **Frame-rate control experiment rules out temporal resolution as the confound:** Tables 4 and 5 show that human accuracy degrades from 95.6% at 30 FPS to 0% at 1 FPS, while all VLMs remain at 0% across all tested frame rates (1–30 FPS). This is the correct experiment, and its outcome strengthens the paper's core diagnostic.

4. **Deterministic, reproducible benchmark with principled SNR characterization:** Algorithms 1–2 fully specify the generation procedure, and Table 2 provides quantitative SNR metrics (basic, perceptual, temporal coherence, motion contrast) across all three categories. The dataset is released alongside generation code, evaluation scripts, and fine-tuning configurations.

---

## Weaknesses

### Fatal
None.

### Major

- **Section 3.3.2 contains internally inconsistent numbers that are irreconcilable with the main results.** The text states: "words exhibited negligible detection (~0%) below 2.5 dB SNR, but jumped to 85.7% accuracy above this threshold." It then adds: "Prompts performed best (40% accuracy), with Chain-of-Thought reasoning improving general identification tasks compared to direct prompting." However, Figure 4's data table shows accuracy jumping from 0.00 to 1.00 (100%) above the threshold — not 85.7%. More critically, the sentence about prompts performing at "40% accuracy" invokes VLM prompting language, yet Table 1 shows every VLM at 0% under every prompting condition, and Table 5 confirms 0% at all frame rates. The figure is captioned "Analysis of effects of SNR on detecting words with *direct prompting and chain of thought prompting*," suggesting it depicts VLM performance — but if so, these non-zero values contradict the paper's main claim. If Figure 4 actually shows *human* performance at varying SNR (which would be the scientifically coherent interpretation), then the figure title is mislabeled and the sentence about prompting strategies is misplaced. This inconsistency must be resolved; as written, it introduces genuine doubt about whether some models achieve non-zero accuracy under specific SNR conditions.

- **The paper frames motion-defined form perception as synonymous with "temporal understanding" generally, an overreach the evidence does not support.** SpookyBench stimuli require exactly one capability: computing a temporal optical-flow or differencing signal and grouping pixels by flow direction (motion-defined form / structure-from-motion). The paper's conclusion that current architectures are fundamentally "time-blind" generalizes a specific low-level perceptual gap into a claim about temporal reasoning broadly. Current Video-VLMs do demonstrate meaningful temporal reasoning on other tasks — event ordering, action recognition, temporal grounding, causal event reasoning — precisely because those tasks allow reasoning over spatially interpretable frames. Section 5's architectural prescriptions ("dedicated temporal coherence pathways") and the title's framing of "time blindness" suggest a broader diagnosis than SpookyBench can support. A defensible claim is that current architectures cannot perform *motion-defined form perception* because they never compute temporal derivatives over densely sampled video; that is already a strong, novel finding without requiring the stronger claim.

### Minor

- **The effective number of frames actually ingested by VLMs at 30 FPS is undocumented.** A 7-second video at 30 FPS yields ~210 raw frames; most VLMs apply internal token budgets or frame caps (typically 8–32 frames), which may reduce effective FPS to the range where humans also fail (Table 4: humans fail at 1 FPS, degrade substantially at 5–10 FPS). The paper states models were evaluated "using identical temporal downsampling" but does not document the actual frame counts presented to each model at the 30 FPS setting. The fine-tuning finding (0% after targeted training) partially absorbs this concern, but documenting effective frame counts — even in a table footnote — would remove ambiguity from what is otherwise the paper's most important control experiment.

- **The fine-tuning analysis does not report training-set accuracy.** The paper observes that "fine-tuned models produced outputs that mimicked training examples without correctly identifying test patterns" (Section 5), but does not check whether fine-tuned models achieve >0% on the 400 training videos. If training accuracy is high but test accuracy is 0%, this directly demonstrates perceptual memorization without genuine visual processing and constitutes the strongest possible version of the architectural-limitation argument. If training accuracy is also 0%, that is a qualitatively different finding with different implications.

- **Model count inconsistency:** The abstract and introduction state "15 state-of-the-art Video-VLMs," but Table 1 includes approximately 27 models (24 open-source + 3 closed-source). This does not undermine the scientific contribution — the evaluation is more thorough than claimed — but the stated count should match the table.

### Trivial
None beyond the model count issue noted above.

---

## Nice-to-Haves

- An optical flow baseline (e.g., RAFT + motion segmentation classifier) applied to SpookyBench videos would establish that the benchmark *is solvable* with the right processing, converting the paper's argument-by-absence into a concrete architectural diagnosis: the benchmark requires flow computation, VLMs fail because they don't compute flow, and a flow-based method achieves near-perfect accuracy. This would be a strong addition without changing the main findings.
- The human evaluation used only 6 participants. While results are consistent and the effect is very large, a larger cohort (20–30 participants) would better characterize individual variation, especially for the Dynamic Scenes category where one annotator achieved 91.2% while another achieved 99%.
- Section 3.3.2 discusses parallels to medical imaging diagnostics (mammography microcalcifications, SNR step-function behavior). This analogy is interesting but the implications for adversarial attacks on real-world systems (road signs, medical labels) are stated briefly without evidence — these would be worth expanding or qualifying.

---

## Removed Points
*These points are flagged to be removed; treat them with caution.*

- **Harsh Critic: "motivating examples (firefly bioluminescence, Morse code) do not encode information via motion-defined form."** The paper uses these as thematic motivators for why temporal-only encoding matters, not as examples of the exact same perceptual mechanism. This is rhetorical framing, not a scientific error. Removed as scope creep.

- **Harsh Critic: "the paper's claim to be the 'first benchmark that exclusively evaluates a model's ability to process and understand pure temporal information' should be narrowed."** The REMOVE rule for missing related works applies; we cannot confirm other benchmarks exist without external sources. Removed.

- **Strength Finder: "Insightful connection to neuroscience."** The neuroscience framing in Section 2.2 is motivational background, not a concrete contribution. The distributed-neural-timing discussion does not translate into an actionable experimental or methodological element. Removed as generic.

- **Harsh Critic: underanalysis of fine-tuned model output types** (whether models parrot training labels vs. produce random outputs). This would strengthen the paper but is a nice-to-have; the 0% test accuracy is the substantive finding regardless.

---

## Novel Insights

The most genuinely novel insight is not just that VLMs fail at temporal tasks, but that the failure persists completely through fine-tuning — the models cannot learn to solve the task even with direct exposure to the distribution. This distinguishes SpookyBench from benchmarks where fine-tuning closes the gap, and it suggests the deficit is not addressable by data or training-objective changes alone within the current architectural paradigm of spatial-feature-first processing. Combined with the frame-rate experiment showing that the failure is not merely a temporal-resolution issue, the paper's evidence converges on a specific architectural bottleneck: the absence of any mechanism to compute coherent motion signals before visual features are extracted from individual frames.

---

## Suggestions

1. **Resolve Section 3.3.2 immediately:** Determine whether Figure 4 depicts human or VLM accuracy, correct the figure caption accordingly, and remove or re-anchor the 85.7% and 40% statistics so they correspond to identifiable conditions in the paper.
2. **Narrow the "time blindness" framing** to "motion-defined form perception" or "structure-from-motion" throughout, especially in the title, abstract, conclusion, and Section 5's architectural prescriptions. This is more precise and actually stronger scientifically.
3. **Add a table column documenting effective frame counts** for each model at the nominal 30 FPS setting (or at minimum the four frame-rate-tested models). This is low-effort and closes a genuine gap in the experimental documentation.
4. **Report fine-tuning training-set accuracy** alongside test accuracy to distinguish memorization from perceptual failure.
5. **Correct the model count** in the abstract and introduction from "15" to the actual number evaluated.

---

## Evaluation on Key Axes

- **Originality:** High. The benchmark design — encoding content purely through opposing motion in binary noise — is a genuinely novel experimental instrument with no prior analog in the VLM evaluation literature.
- **Importance of research question:** High. Temporal processing is a known weak point of current VLMs; SpookyBench isolates it more cleanly than existing benchmarks.
- **Claims well-supported:** Moderate. The zero-accuracy finding is solidly supported; the "time blindness" framing is broader than the evidence warrants, and Section 3.3.2 introduces unexplained inconsistencies.
- **Soundness of experiments:** Moderate-to-good. Model evaluation is thorough; fine-tuning and frame-rate experiments are well-designed; but the effective FPS gap and the Section 3.3.2 inconsistency are real issues.
- **Clarity of writing:** Moderate. Most of the paper is clear, but Section 3.3.2 is genuinely confusing in a way that creates factual ambiguity about the results.
- **Value to the research community:** High. The benchmark is released with code, and the finding (architectural failure persisting through fine-tuning) is actionable for future architecture design.

---

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>4</originality>
<importance>4</importance>
<claims_supported>3</claims_supported>
<soundness>3</soundness>
<clarity>3</clarity>
<community_value>4</community_value>
</subscores>