Now I'll produce the final review.

## Summary
This paper introduces MotionCritic-DB, a large-scale human perceptual evaluation dataset with 52.6K preference annotations on 73K generated motions, and MotionCritic, a learned critic model that predicts motion quality in alignment with human judgments. The critic model convincingly outperforms existing metrics (85.07% vs. 71.78% best baseline on human-preference alignment) and generalizes across different generators and to real motion data. The paper also presents preliminary fine-tuning results using the critic as supervision for improving generation quality.

## Strengths
- **Large-scale, carefully curated preference dataset.** MotionCritic-DB contains 52.6K annotations on 73K motions — ~37× larger than the closest prior work (MoBERT, 1.4K motions). The annotation pipeline is rigorous: multiple-choice format with "all good"/"all bad" options, pilot testing, 90% quality-control threshold, and a consensus experiment showing 82.37% unanimous decisions and 90% pairwise agreement among 10 subjects. This convincingly validates that human perceptual judgments of motion quality are consistent across subjects (Section 3.3, Figure 2).

- **Critic model substantially outperforms all prior metrics on human-alignment.** In Table 1, MotionCritic reaches 85.07% accuracy on the MDM test set and 81.43% on the FLAME test set, while the best prior metric (Person-Ground Contact) achieves 71.78% and 69.82%, respectively. The gap is large and consistent, directly supporting the paper's central claim of a more human-aligned metric.

- **Critic model generalizes to ground-truth motion and reveals dataset artifacts.** The paper groups HumanAct12 GT motions by critic score and shows (both quantitatively and qualitatively) that the lowest-scoring group contains genuine artifacts (jittering, floating). Critic score correlates with human Elo ratings while FID does not (Figure 4). This demonstrates a practical use case (dataset diagnosis) beyond the training distribution.

- **Fine-tuning with the critic shows promising results with minimal compute.** User study results (Figure 5) show monotonically improving Elo ratings as fine-tuning progresses, requiring only 800 iterations (0.23% of pre-training cost). Qualitative visualizations confirm reduction in artifacts.

## Weaknesses

### Major
- **Insufficient evidence that the critic supervision is responsible for fine-tuning improvements.** The fine-tuning experiments lack essential baselines: (a) continued training of MDM *without* the critic (to separate improvement from more training vs. the critic signal); (b) alternative supervision signals (e.g., reconstruction loss, heuristic metrics, MoBERT features). Without these, it is unclear whether the critic provides *useful* perceptual supervision or merely incentivizes motions that the learned critic scores highly (a known concern with learned reward models). The paper lists fine-tuning as a core contribution (Claim 3, Section 1), but the evidence is restricted to a single generator (MDM) and dataset (HumanAct12) and does not compare against any alternative. The dataset and metric contributions stand independently, but the fine-tuning claims should be presented as a proof-of-concept or significantly strengthened.

### Minor
- **FID comparison in Figure 4 is not a fair or meaningful test.** The paper groups 1,190 GT motions into 5 subsets of ~238 motions based on critic scores and computes FID per subset. FID is a distribution-level metric requiring large sample sizes for reliable estimation; computing it on ~238 samples is non-standard. The paper's own argument (Section 1) correctly states that FID "does not operate on an instance level," so the claim that "critic score aligns well with human preferences, while FID does not" compares two metrics with fundamentally different design purposes. The framing overstates the finding.

- **No statistical uncertainty reported.** Table 1 reports accuracy and log loss to two decimal places without confidence intervals, standard errors, or any measure of variance. While the accuracy gap is large enough that significance testing would not change the qualitative conclusion, the absence of uncertainty reporting is a methodological gap.

- **Hyperparameters for fine-tuning are listed but not analyzed.** The critic threshold τ=12.0, re-weight scale λ=1e-3, and KL loss scale μ=1.0 are given without motivation or ablation. The effect of the KL regularization term is not isolated, making it unclear whether it is necessary or how it interacts with the critic loss.

- **Softmax conversion for baseline metrics is under-justified.** The paper states it uses softmax "to convert the scores to probabilities (taking the opposite before softmax for metrics where smaller is better)" (line 379). This step is described in a single sentence with no analysis of how it affects metrics with different scales, ranges, or distributions.

- **Training data limited to diffusion-based generators.** The dataset is generated exclusively from MDM and FLAME, both diffusion-based. Motions from VAE, GAN, or VQ-VAE methods — which may produce different failure modes — are not represented. This is a reasonable scope choice but is not explicitly acknowledged as a limitation in the paper.

### Trivial
- None.

## Nice-to-Haves
- Analyze failure cases of the critic model (where does it disagree with human annotators on the held-out test set, and are there systematic patterns?).
- Compare the critic against FID at the distribution level where both metrics are designed to operate (e.g., correlate FID rankings of full test sets across generation methods with user study rankings).
- Ablate design choices in the critic: motion representation (SMPL vs. joint positions vs. velocities), backbone architecture, and number of preference pairs extracted per question.
- Analyze where the proposed metric and baselines disagree (e.g., does Person-Ground Contact capture foot artifacts but miss upper-body issues, while the critic handles both?).

## Removed Points
These points were flagged by the reviewers but are removed or softened after verification against the paper:

- **"User study may not include step 0"** — The figure caption and evaluation protocol ("evaluate every 200 steps") strongly imply step 0 (pre-trained model) is a fine-tuning milestone. This specific sub-claim is not clearly supported by the paper text and is removed.
- **"Missing related works"** — Removed per instructions (cannot verify without external sources).
- **Formatting/typo nitpicks** — Removed as parser artifacts from the PDF extraction process.
- **Reproducibility concerns about hyperparameters** — The paper lists hyperparameters; the lack of ablation is retained as a minor weakness, but demanding full implementation disclosure is a nitpick given conference norms.
- **"Fatal" framing of fine-tuning issue** — The harsh critic framed this as potentially undermining the paper. Since the dataset and metric are the primary contributions and stand independently, the fine-tuning limitation is demoted to a Major weakness.

## Novel Insights
None beyond the paper's own contributions. The key observation — that a learned critic trained on large-scale human preference data can substantially outperform heuristic and error-based metrics for evaluating motion quality — is the paper's own core contribution.

## Suggestions
1. Strengthen the fine-tuning evaluation by adding a baseline with continued training *without* the critic, and ideally with an alternative supervision signal (e.g., heuristic metrics or MoBERT features).
2. Add confidence intervals or error bars to Table 1.
3. Reframe or remove the FID comparison in Figure 4, or compute FID at the distribution level across multiple generators and correlate with user study rankings.
4. Ablate key hyperparameters (τ, λ, μ) and the KL regularization term to isolate their contributions.
5. Explicitly acknowledge the dataset's limited coverage of non-diffusion-based generators as a limitation.

## Score and Decision
MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>