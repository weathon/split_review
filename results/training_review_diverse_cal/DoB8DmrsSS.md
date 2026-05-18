Now I have thoroughly read the paper and verified all claims against the actual text. Let me produce the consolidated review.

---

## Summary

This paper proposes SHIFT, a diffusion-based adversarial state perturbation attack for vision-based RL that goes beyond traditional \(l_p\)-norm constraints. The method combines history-conditioned classifier-free guidance (for realism and temporal consistency), policy-based classifier guidance (to induce target actions), and autoencoder-based realism enhancement. Evaluated against five state-of-the-art defenses across four Atari games, SHIFT significantly reduces cumulative reward and achieves high manipulation rates where prior attacks (PGD, MinBest, PA-AD, high-sensitivity direction attacks) fail, especially against diffusion-based defenses like DP-DQN.

## Strengths

1. **Novel technical combination for the RL attack setting.** The paper is the first to jointly use history-conditioned classifier-free guidance and policy-as-classifier guidance to generate adversarial state perturbations in RL. While the individual components are known in the generative modeling literature, composing them into a working attack pipeline that simultaneously satisfies realism, history alignment, and action manipulation is a nontrivial engineering contribution. Theorem 1 formally states the combined reverse process, and the paper builds on recent EDM-based efficient sampling (Karras et al., 2022) to make the attack practical.

2. **Strong empirical results against state-of-the-art defenses.** Table 1 shows that SHIFT reduces episode reward by more than 50% across all four games against five defenses (SA-DQN, WocaR-DQN, CAR-DQN, Diffusion History, DP-DQN). Critically, Figure 3a demonstrates that prior attacks (PGD, MinBest, PA-AD, PGD TC, blurred/shifting high-sensitivity attacks) all fail to compromise DP-DQN even with large budgets, while SHIFT succeeds. This directly supports the paper's main practical claim: existing \(l_p\)-constrained attacks are insufficient against sophisticated diffusion-based defenses, and semantics-aware perturbations are needed.

3. **Conceptual framing that goes beyond \(l_p\) norms.** The paper introduces formal definitions (valid states \(S^*\), realistic states, semantics-changing states, history-aligned states) that replace the brittle \(l_p\)-ball constraint with semantically meaningful criteria. Although these definitions are not directly computable (and the paper acknowledges this), they provide a useful conceptual vocabulary for thinking about adversarial perturbations in RL that previous work lacked. The \(l_2\) distance analysis in Figure 2 and reconstruction error/Wasserstein distance in Figure 3a offer indirect empirical proxies for the defined concepts.

4. **Practical generation speed via EDM.** Table 2 shows that SHIFT with EDM (~0.2s per perturbed state) achieves comparable attack performance to DDPM while being much faster, a genuine practical improvement over naive diffusion-based attacks.

5. **Useful preliminary probing analysis.** Figure 3b investigates a probing-based defense where the victim occasionally observes true states. The analysis shows the expected trend (more frequent probing improves robustness) and identifies a clear direction for future work on strategic probing.

## Weaknesses

### Fatal
None.

### Major

1. **Overclaim on "breaking all known defenses."** The paper states that "SHIFT can break all known defenses" (line 20) and that prior attacks "cannot compromise these more advanced defenses" while SHIFT does (lines 16–17). The evaluation covers five defenses (SA-DQN, WocaR-DQN, CAR-DQN, Diffusion History, DP-DQN) on four Atari games. ATLA is explicitly acknowledged as too expensive to evaluate. Defenses based on certified robustness, randomized smoothing, or alternative state verification are not discussed. The "all known defenses" claim is not supportable from the evidence presented and should be replaced with a precise scope statement.

2. **Insufficient direct evidence that generated states are truly semantics-changing.** The paper's central claim is that SHIFT succeeds because it generates "semantics-changing" perturbations (as opposed to \(l_p\)-constrained noise). However, the primary evidence is indirect: (a) manipulation rate (the victim takes the target action) and (b) anecdotal examples in Figure 1. Manipulation rate conflates effect with definition — an attack that exploits high-sensitivity directions (Korkmaz, 2023) can also achieve high manipulation rates without changing semantics. Direct measurement of semantic content — e.g., extracting game state variables (ball/paddle positions in Pong, chicken positions in Freeway) from pixels and quantifying whether these change — would validate the core claim. The \(l_2\) distance analysis in Figure 2 shows SHIFT states are *close* to true states, which if anything suggests *less* semantic change (though small \(l_2\) changes can in principle alter semantics via diffusion). Without direct semantic measurement, it remains unclear whether SHIFT's success comes from genuine semantic manipulation or from exploiting policy sensitivity to features that happen to satisfy the diffusion model's realism constraints.

3. **Disconnect between formal definitions and operational implementation.** The paper establishes an elegant formal framework centered on the set of valid states \(S^*\) and projections onto it (Definitions 1–5), then claims the generated states satisfy realism, semantic change, and history alignment relative to these definitions. However, \(S^*\) is never computed — the paper acknowledges this is intractable (line 96). The operational proxies (diffusion model output for realism, autoencoder reconstruction error, conditioning on true history for alignment) are never validated against the formal definitions. For example, Definition 3 defines semantic change as \(\text{Proj}_{S^*}(\tilde{s}) \neq s\), but the paper never computes or approximates this projection. The formalism thus plays a rhetorical rather than analytical role. While approximate operationalization is common and acceptable, the paper presents the definitions as a core contribution and claims that "our attack is able to generate realistic perturbed states that are semantically different from the true states" (line 104) without ever directly measuring these properties as defined. This gap between claimed contribution and verified evidence weakens the theoretical framing.

### Minor

1. **No ablation of the individual guidance components.** The method combines three elements: history-conditioned diffusion (classifier-free guidance), policy guidance (classifier guidance), and autoencoder realism guidance. Table 2 only ablates DDPM vs. EDM architecture. The contribution of each guidance component — and their interaction — is not isolated. Understanding which component drives the attack's success (especially against different defense types) would substantially strengthen the paper.

2. **Real-time feasibility assumption requires discussion.** SHIFT generates a perturbed state in ~0.2s with EDM. Atari frames are typically rendered at ~0.02–0.05s per frame (20–50ms). A 0.2s generation time means the attack cannot be applied at every step in a real-time setting. The paper says the attack "remains feasible for real-time applications" (line 214) without addressing this gap. The authors should clarify whether the attack is applied at reduced frequency, or what real-time assumption they are making.

3. **Single reference policy for training.** The diffusion model is trained on trajectories from a single reference policy \(\pi_{ref}\) (line 136). The mismatch between \(\pi_{ref}\)'s state distribution and the victim's distribution (especially a robust victim's) could affect attack transferability. The paper evaluates against multiple defense victims but uses only one reference policy for training, leaving open the question of how sensitive the attack is to the training data distribution.

4. **Probing experiment under-specified.** The probing analysis (Figure 3b) is presented as a "preliminary defense strategy," which is appropriate. However, the paper states that the victim uses "a combination of historical true states and perturbed states to infer the current state" (line 216) without specifying how this combination works. Since this affects interpretation of the results, more detail is needed.

5. **No statistical significance testing.** Table 1 reports means and standard deviations over 10 runs, but no significance tests are provided for comparisons between defenses or between SHIFT and baselines in Figure 3a. Given the inherent variability in RL, this limits confidence in the reported differences.

### Trivial

- **Theorem 1 justification is terse.** The paper claims the two guidance mechanisms "can coexist without interference" because the noise prediction depends on \(\tau_{t-1}\) while the gradient depends on \(\bar{a}_t\). This is a standard property of score-based guidance composition, but the brief justification in the main text (lines 161–163) could be expanded, especially since the gradient \(\nabla_{\tilde{s}_t^i}\log\pi(\bar{a}_t|\tilde{s}_t^i)\) is evaluated at a sample that arises from the history-conditioned process. The claim is not wrong — it follows from the standard derivation in (Dhariwal & Nichol, 2021) — but a more complete derivation would be helpful.

## Nice-to-Haves

- **Direct measurement of semantic change** using game state variable extraction from pixels (e.g., object positions, velocities) to quantify how much SHIFT actually alters semantics vs. exploiting feature sensitivity.
- **Ablation study** isolating the contributions of history conditioning, policy guidance, and autoencoder guidance.
- **Broader evaluation** across more victim policies (different random seeds, hyperparameters) to assess attack transferability.
- **Discussion of attack frequency** in real-time settings given the 0.2s generation time vs. Atari frame rate.
- **Statistical significance tests** for the main comparisons.

## Removed Points

- **"ATLA is acknowledged as too expensive to evaluate... the paper does not discuss defenses based on certified robustness, randomized smoothing, or state verification"** — This criticism is packaged as part of the "overclaim" issue, which is retained. The standalone complaint about missing specific defense types is removed because the paper covers the most relevant defenses in the attack literature and the criticism would only matter if the paper hadn't overclaimed in the first place. The overclaim itself is the real problem.
- **Strength Finder's generic praise** (e.g., "important problem") — Not present in the Strength Finder output; all listed strengths are paper-specific. Kept as-is.
- **Criticism about the probing experiment being "not a substantial result"** — Retained but downgraded to a minor point about under-specification, since the paper explicitly labels it as "preliminary."
- **"The paper needs a direct measure of semantic difference... For Atari games, one could extract game state variables"** — Retained as Major weakness #2; it's a valid and feasible suggestion.

## Novel Insights

None beyond the paper's own contributions. The reviews confirm that the paper's main novelty lies in the practical combination of diffusion guidance techniques for adversarial perturbations in RL, while also identifying that the formal framework and the empirical validation of "semantic change" are weaker than they appear at first glance. A genuinely novel insight from the review process is that the paper's strongest contribution may be empirical (demonstrating that diffusion-based attacks can break state-of-the-art defenses) rather than theoretical, and the formalism might better serve as motivation rather than as a verified contribution.

## Suggestions

1. **Temper the scope claims.** Replace "break all known defenses" with a precise statement of what was evaluated and under what conditions (e.g., "breaks five state-of-the-art defenses including diffusion-based ones on four Atari games").
2. **Add direct evidence of semantic change.** Use an auxiliary oracle or game-state extraction tool to measure whether object positions, velocities, or other semantic variables actually change under SHIFT vs. baselines.
3. **Ablate the guidance components.** Run variants without history conditioning, without policy guidance, and without autoencoder guidance to isolate each component's contribution.
4. **Address the real-time feasibility gap.** Either specify the assumed attack frequency or acknowledge the limitation.
5. **Provide more detail on the probing experiment's state inference method.**

## Score and Decision

The paper presents a novel attack with strong practical results that convincingly demonstrate a real vulnerability in current RL defenses. The main weaknesses are an overclaim about the scope of defenses broken, insufficient direct evidence for the "semantic change" claim that is central to the paper's narrative, and a gap between formal framing and operational implementation. These are real but addressable — they do not invalidate the core contribution (a working attack that breaks existing defenses). The paper would benefit from tempering its claims and adding direct semantic measurements, but as submitted it offers a meaningful advance.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>