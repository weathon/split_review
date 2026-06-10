I have read the paper thoroughly and cross-referenced all reviewer claims against the actual text. Let me construct the final review.

## Summary

This paper investigates how the dimension over which scaled dot-product attention is applied (spatial vs. channel-row vs. channel-column) affects the sample efficiency of PPO on 56 Atari games. The authors design four self-attention modules (SWA, CWRA, CWCA, CWRCA), integrate them between CNN layers, and evaluate aggregate and per-game performance alongside an interpretability study on Pong. The results show that all variants perform similarly to the baseline on aggregate (overlapping CIs), with CWCA slightly better and CWRCA slightly worse, and that per-game winners differ across environments.

## Strengths

1. **Systematic permutation of attention dimensions beyond prior work.** Prior work (Manchin et al., 2019) explored only one way to integrate self-attention into PPO. This paper isolates which tensor dimensions (spatial, channel-row, channel-column) the dot-product operates over, creating four distinct modules (Section 4, Figure 1). This ablation is a clean and useful research design.

2. **Larger-scale evaluation than comparable prior work.** Evaluating on 56 Atari games with 5 seeds each (Section 5.1) is more extensive than Manchin et al.'s 10 games × 3 seeds. The use of Agarwal et al. (2021)'s recommended metrics (IQM, stratified bootstrap CIs, performance profiles) follows community best practices for reliable RL evaluation.

3. **Interesting artifact analysis in the interpretability study.** The finding that different attention modules create characteristic artifact patterns in feature maps (horizontal bars from CWCA, vertical bars from SWA, both from CWRCA in Figure 6) and that these artifacts correlate with exploration behavior (Table 1) is a genuinely novel observation, even though the study is narrow.

## Weaknesses

### Major

1. **Gap between the paper's rhetoric and its evidence.** The abstract and introduction frame the paper around self-attention "enhancing sample efficiency" and "distinct impacts," but the central aggregate result is that all five agents (including the no-attention baseline) have statistically indistinguishable performance — the paper itself states "most CIs overlap" (Figure 2 caption), "relatively small differences" (line 89), and "no stochastic dominance" (line 95). The paper does note these facts in the body, but the abstract/conclusion do not reflect the null aggregate result. The claim of "distinct impact" overstates what the evidence supports; the data show, at best, very subtle differences (CWCA marginally better, CWRCA marginally worse) against a background of overlapping CIs.

2. **The inductive-bias claims are supported by post-hoc game selection.** The paper's main per-game claim is that different attention modules help in games with matching movement dynamics (e.g., CWRA for horizontally scrolling ChopperCommand, CWCA for vertically scrolling Zaxxon). However, these games are selected by picking, for each attention variant, the game where it has the "highest winning margin" and "relatively lower standard error" out of 56 games (lines 99-106). With 56 games and 5 seeds, some games will favor any given variant by chance. No correction for multiple comparisons, no preregistered hypotheses, and no statistical test distinguishing genuine interaction from noise are provided. The paper is transparent that this is "heuristic" (line 99), but the claims in the conclusion and abstract do not carry this qualification.

3. **The interpretability study is too narrow to support the conclusions drawn from it.** The analysis (Section 5.3) is conducted on a single game (Pong) at a single checkpoint (3M steps), using a single selected run per agent (chosen to "resemble its mean performance the most") and 10 observations (only 1 shown). The claim that vertical attention artifacts "could slow down the learning process" (Figure 6 caption) is based on visual inspection of Grad-CAM heatmaps, which provide coarse spatial localization. The exploration analysis uses mean standard deviation of actor logits over 10 observations — a tiny sample for characterizing a stochastic policy. The paper acknowledges this is an "initial case study" (line 120), but the conclusions Section 6 generalizes from it without caveats.

### Minor

4. **No baseline reproducing Manchin et al. (2019)'s design.** The paper is explicitly "inspired by Manchin et al. (2019)" and defines itself in contrast to that work (Section 2), but does not implement Manchin et al.'s self-attention design as a baseline. Since differences in implementation details (not just attention dimension) could explain performance variation, including this baseline would anchor the contribution more firmly. The omission is notable given that Manchin et al. reported improvements on a subset of Atari games.

5. **Underreported experimental details.** The paper uses RL Baselines3 Zoo (line 77) but does not report the specific PPO hyperparameters, CNN architecture details (number of channels, kernel sizes, strides), or training protocol (frame skip, reward clipping, sticky actions). These matter for reproducibility, especially when comparing architectural variants. The paper also does not clarify whether the 5 random seeds differ in environment seed, network initialization seed, or both (line 77).

6. **Missing per-game results table.** The paper states it "summarize[s] the list of games won by each agent" (line 99) but only shows 4 cherry-picked examples (Figure 4). A full table of sample means and standard errors across all 56 games would allow readers to evaluate the inductive-bias claims directly rather than relying on selected favorable examples. The paper could place such a table in the main text or (deleted by parser) appendix.

7. **CWRCA is not a genuinely distinct attention operation.** As the paper explicitly states (line 61), CWRCA is simply the element-wise sum of CWRA and CWCA outputs. Treating it as a distinct module with its own "inductive bias" separately from its components is somewhat misleading — its bias is a linear combination of the other two. This is a minor framing issue since the paper does disclose the design.

### Trivial

- None.

## Nice-to-Haves

- Adding computational cost metrics (parameter counts, FLOPs, training time per module) would strengthen the practical contribution, since the paper mentions computational efficiency as a design motivation (Section 4).
- The inductive-bias story would be much stronger if the authors stated their predictions ex ante (e.g., "CWRA will outperform on horizontally scrolling games A, B, C; CWCA will outperform on vertically scrolling games X, Y, Z") and then tested those predictions statistically, rather than selecting the best game per variant ex post.

## Removed Points

These points were raised in the reviews but removed after verification against the paper:

- **"Opening paragraph is generic and overly long" / "Line 12 is grammatically incomplete"** — REMOVED: The "fragment" on line 12 is a parser artifact from PDF extraction (the sentence continues from line 10). Formatting/style critiques are not substantive weaknesses.
- **"Evaluation metric systematically biases toward null result"** — REMOVED (from Fatal/Major tier): The paper justifies using mean evaluation score over the entire period as favoring sample efficiency (line 84). Whether this is the optimal choice is debatable, but calling it a "systematic bias" is an overstatement — the metric would still detect genuine differences. This is at most a minor methodological preference. (Kept as a note but not a retained weakness.)
- **"No discussion of computational cost"** — MOVED to Nice-to-Haves, as it is not a core flaw for an empirical study focused on sample efficiency.
- **"No analysis of training variance across seeds"** — REMOVED: The paper reports stratified bootstrap CIs which inherently account for variance across runs.
- **Strength: "Empirical correlation between inductive biases and game dynamics"** — REMOVED: This strength conflicts with the verified Weakness #2 (post-hoc selection). The correlation claimed is circular: games were selected because the agent performed well on them, then explained post-hoc.
- **Critique about "Model-based RL critique being generic"** — REMOVED: The paper is scoping out model-based RL, which is acceptable; this is a related work section, not a main contribution.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Honestly frame the null aggregate result in the abstract and conclusion.** The finding that all attention variants perform similarly to baseline on aggregate is a legitimate result. Presenting it as such, rather than overclaiming "distinct impacts," would make the paper more credible.
2. **Provide the full per-game results table** (all 56 games, all agents, means and standard errors) either in the main text or as supplementary material, so readers can evaluate the inductive-bias claims directly.
3. **State inductive-bias predictions ex ante** and then test them systematically (e.g., pre-specify which game types should favor which module, then count/measure how many of the predicted patterns actually hold).
4. **Add the Manchin et al. attention design as an explicit baseline** to anchor what the dimension permutation adds beyond the closest prior approach.
5. **Expand or caveat the interpretability study.** Either run it on more games and checkpoints, or explicitly state that the results are preliminary observations from a single case study and should not be generalized without further evidence.

## Score and Decision

The paper asks a reasonable question and runs a systematic experiment, but the central claims substantially outrun the evidence. The aggregate result is a null result (no significant differences), and the per-game inductive-bias claims rely on post-hoc selection of favorable examples without statistical validation. The interpretability study is too narrow to support the conclusions drawn from it. While the paper has a legitimate empirical contribution (the systematic dimension permutation and the artifact analysis), the framing needs substantial revision to match what the evidence actually supports.

<score>4.5</score>
<decision>Reject</decision>