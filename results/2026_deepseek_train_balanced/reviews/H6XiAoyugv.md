## Summary

This paper proposes VSSC (Visible, Semantic, Sample-specific, Compatible) triggers for backdoor attacks, along with an automated pipeline using LLMs for trigger selection, generative models for trigger insertion, and VLMs for quality assessment. The key idea is that visible but semantically compatible triggers can simultaneously achieve stealthiness (through compatibility rather than invisibility), robustness to visual distortions, and deployability in physical scenarios. The method is evaluated across three tasks (image classification, object detection, face verification) in digital, digital-to-physical (print-and-recapture), and physical settings.

## Strengths

- **Compelling D2P robustness evidence**: The digital-to-physical (print-and-recapture) results are the paper's clearest empirical contribution. On ImageNet-Dogs, VSSC achieves 97.62% ASR under print-and-recapture while baseline attacks collapse to near-zero ASR (Table recapture.tex, line 294). This is a non-trivial result that directly supports the paper's central thesis that visible+semantic triggers are inherently more robust to visual distortions than invisible/patch-based triggers.

- **Three-task, three-scenario evaluation is genuinely comprehensive**: The paper evaluates across image classification, object detection, and face verification, with digital, D2P, and physical scenarios for each. The face verification results (98.98% digital, 94.47% D2P, 91.64% physical at just 1% poisoning, line 386-395) are particularly strong and demonstrate versatility beyond simple classification.

- **Grad-CAM analysis provides mechanistic insight**: Figure 8 (lines 553-555) shows that under Gaussian blur, JPEG compression, and noise, the attention region of VSSC-backdoored models stays on the trigger, while BadNets and TrojanNN attention regions shift away. This provides evidence for *why* VSSC maintains ASR under distortion: the model learns semantic trigger features rather than low-level pixel patterns.

- **Honest discussion of semantic trigger limitations**: Section 5.1.2 (lines 422-476) candidly addresses the inherent constraint that no single semantic trigger is compatible with all classes in diverse datasets, and offers two processing strategies. This level of self-critique is rare and strengthens the paper's credibility.

## Weaknesses

### Major

- **Human inspection study uses asymmetric task designs that invalidate cross-method comparisons**. For VSSC, participants distinguish poisoned images (synthetic harness) from benign images that *already contain a harness* — a hard perceptual task. For baseline attacks, participants distinguish poisoned images from *random benign images* — an easier task (lines 508-511). The paper then directly compares the fooling rates (VSSC 51.3% vs. Blended 1.9%) as if the tasks were equivalent. They are not. The reported numbers conflate task difficulty with attack stealthiness. A valid comparison would hold the discrimination task constant across methods (e.g., test all attacks against benign images from the same distribution). As published, the human study's primary quantitative comparison is uninterpretable.

- **The LLM-based trigger selection module is presented as a core contribution but is not validated against any non-LLM baseline.** The coarse-grained selection uses GPT-4 with the prompt "Find 10 common objects which look natural with [classes]" (line 169). There is no experiment showing that LLM-selected triggers outperform triggers chosen by a simple rule (e.g., the 10 most common nouns in the dataset's visual domain) or random selection. Since GPT-4 API access is a real cost, the practical question "what does the attacker pay for?" goes unanswered. The ablation in Section 5.1.2 validates only the *fine-grained* ISR-based filtering; the LLM itself is not ablated. This weakens the claimed contribution of the trigger selection module as a scientific advance rather than an implementation convenience.

### Minor

- **No statistical variance reported for any result despite a stochastic pipeline.** The entire pipeline has randomness at multiple levels: generative model outputs vary across runs, VLM assessments have stochasticity, LLM outputs may vary, and some images are discarded after failed generation attempts (line 203-204). Yet every table reports single numbers without confidence intervals, standard deviations, or per-run breakdowns. With small poisoning ratios (1–10%) used in some experiments, variance could be substantial. This makes it impossible to assess whether observed differences between VSSC and baselines are statistically meaningful.

- **The physical scenario evaluation conflates the claim of "automated manpower-free attack" with what is actually automated.** The paper claims to "liberate physical backdoor attacks from reliance on manpower" (line 50). The pipeline automates *training data generation*. However, for physical scenario *testing*, the authors manually capture 100 real photos per trigger (line 300), place physical objects, and deal with lighting conditions — the exact manual labor the method claims to eliminate. While this is standard evaluation practice, the framing overstates what is automated. The claim is about training data; the evaluation still requires substantial manual effort, and no analysis quantifies how much labor is saved relative to prior physical attacks.

- **Missing analysis of QAM error modes.** The ablation showing QAM improves ASR by up to 10.11% (Figure 6, line 488) is meaningful. However, the paper does not analyze the VLM's false negative rate (good poisoned images discarded), false positive rate (poor images passed), or potential biases toward certain trigger types. Since VLMs are known to hallucinate and have blind spots, these are relevant unknowns for understanding the pipeline's reliability.

- **ISR threshold (0.5) is stated but not ablated.** The threshold for fine-grained trigger selection is set to 0.5 (line 265) with no sensitivity analysis. The relationship between ISR threshold, trigger quality, and downstream ASR is not explored.

### Trivial

- None that warrant mention beyond the above.

## Nice-to-Haves

- A controlled experiment that varies *compatibility* while holding the *trigger constant* would directly test the core mechanistic claim that semantic compatibility (not just visibility) drives stealthiness.
- A quantification of the domain gap between synthetic training triggers and real test triggers (e.g., measuring how ASR varies with photorealism of the generative model) would strengthen the physical scenario claims.
- An analysis of trigger placement consistency across training images and its effect on backdoor learning would be a meaningful extension.

## Removed Points

These points from the inputs were removed with brief justification:

1. **"Physical scenario evaluation contains a fundamental circularity"** — The critic claimed the evaluation is unfair because VSSC uses synthetic training data with real test data while baselines use real data for both. This misreads the paper: VSSC's pipeline is designed for *automated* training data generation; physical testing with real photos is a standard evaluation protocol, not a confound. The paper does not claim to automate testing. The domain gap is a real concern but not a "circularity" or a fatal flaw.

2. **"QAM evaluation conflates VLM capability with attack effectiveness"** — The critic's questions about false positive/negative rates and VLM biases are reasonable research questions but are speculative rather than identified problems in the paper. The paper's ablation (with vs. without QAM) is a valid comparison; requesting detailed error analysis is a nice-to-have, not a weakness per se.

3. **"No analysis of trigger placement" and "No analysis of poisoning ratio sensitivity"** — The paper does vary poisoning ratios (5%–30% in Table physical.tex, line 302) and the critic's claim that "the detection and face verification experiments fix the ratio" is accurate but does not rise to the level of a weakness — it is a scope choice. Trigger placement analysis would be an extension, not a missing requirement.

4. **"Attack cost not discussed"** — Requesting cost analysis (API fees, regeneration attempts) is reasonable but is a discussion point rather than a weakness that undermines the paper's claims.

5. **Various formatting/style/presentation nitpicks** — Removed per filtering rules.

## Novel Insights

None beyond the paper's own contributions. The reviews did not surface a new pattern or connection that the paper itself does not articulate.

## Suggestions

1. **Fix the human study before any publication.** The cleanest fix is to either (a) test all attacks against the same type of benign images (either all with naturally occurring objects or all without), or (b) if the current design is retained, explicitly frame it as two separate tasks and remove the cross-method comparison of fooling rates.

2. **Add an ablation of the LLM trigger selection** comparing LLM-selected triggers against a simple non-LLM baseline (e.g., pick the 10 most visually plausible nouns from a captioning model or a frequency list). This would validate the claimed contribution of the trigger selection module.

3. **Report confidence intervals or standard deviations** for at least the main results. Given the pipeline's stochasticity, this is important for interpretability.

4. **Ablate the ISR threshold** to show how sensitive results are to this hyperparameter.

## Score and Decision

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>