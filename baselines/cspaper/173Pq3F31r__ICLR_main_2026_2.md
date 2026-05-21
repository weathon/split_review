---
job_id: 986d4fc2-cdcb-461f-ad8a-164b494670e6
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: 173Pq3F31r.pdf
paper: Bridging Piano Transcription and Rendering via Disentangled Score Content and Style
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, it studies representation learning, generative modeling, and sequence modeling for symbolic music, with a particular emphasis on disentangling content and style representations.

## Minimum Quality
Pass ✅. The submission contains all core components expected of a research paper, including abstract, introduction, related work, methodology, experiments, results, and conclusion, and it presents a technically coherent method with substantial empirical evaluation, even though I have concerns about novelty, evaluation design, and some methodological underspecification.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find any hidden instructions, suspicious prompts, or other manipulative content targeting automated reviewers in the provided paper text or figures.

# Expected Review Outcome:
## Summary
This paper proposes a unified transformer-based framework for two inverse symbolic music tasks, expressive piano performance rendering (EPR) and automatic piano transcription (APT). The central idea is to learn disentangled note-level score content representations and a global performance style representation, train the model jointly on paired and unpaired data, and then use a separate diffusion-based performance style recommendation (PSR) module to generate style embeddings from score content alone. The paper evaluates the system on ASAP and ATEPP using objective metrics, listening tests, style-transfer demonstrations, and latent-space analyses.

## Strengths
The paper tackles an interesting joint formulation. Modeling EPR and APT together is conceptually well motivated because the two tasks are inverse transformations, and the framework in **Figure 1** communicates this relationship clearly. In particular, the architecture diagram makes the intended factorization easy to follow: score encoder and performance encoder feed a shared content notion, while the style encoder supplies a global control signal for EPR. That is a sensible design choice, and it is more compelling than treating the system as just two loosely connected task heads.

The paper also addresses a practically relevant limitation in prior EPR work, namely dependence on note-level alignment. The proposed Seq2Seq formulation only requires sequence-aligned data, which is useful for scaling to noisier real-world corpora. Even if the underlying components are familiar, the integration is thoughtful and relevant to the MIR community.

The experimental section is broader than average for this topic. The paper includes objective APT results, objective EPR statistics, alignment-based EPR accuracy, subjective listening tests, style-transfer evaluation, and representation analysis. In **Table 1**, the APT results show that the method is competitive with the strong end-to-end baseline of Beyer and Dai (2024), especially on several structure- and notation-related metrics such as \(E_{\text{const}}\), \(E_{\text{offset}}\), and the ScoreSimilarity spelling/staff-related measures. This supports the claim that the learned latent representation is at least useful for transcription, even though it is not uniformly best.

For EPR, **Table 2** is also a genuine strength. The comparison against both alignment-based baselines and an EPR-only ablation is useful. The fact that **Ours (Target)** improves over **EPR-Only** on KL and MAE for duration and velocity suggests that joint training is doing something nontrivial beyond simple architectural scaling. That is one of the more convincing pieces of evidence in the paper.

The disentanglement analyses are imperfect, but still informative. **Table 4** shows a very large gap between style-based and content-based identification for both performer and composer, which is at least consistent with the intended separation. Likewise, **Figure 3** gives a reasonable qualitative picture that the style embeddings organize non-randomly by composer and performer.

The paper is generally readable. The motivation is easy to understand, the tasks are introduced cleanly, and the figures help the reader navigate a fairly large system.

## Weaknesses
1. **The main contribution feels more like a careful combination of existing ingredients than a clear methodological step forward, and the paper does not sufficiently sharpen what is truly new.**  
   The core system combines a transformer Seq2Seq setup, a latent content/style split, KL regularization on the style code, masked reconstruction, and a diffusion model for conditional style generation. Each of these ingredients is individually standard, and the paper's novelty rests mainly on their joint application to EPR and APT. That can still be publishable, but then the paper needs much stronger evidence that the joint formulation yields capabilities or performance that could not be obtained by more modular alternatives. Right now, the empirical story is mixed. On APT in **Table 1**, the method is not clearly superior to the strongest baseline across metrics. On EPR in **Table 2** and **Table 3**, the gains are selective rather than dominant. So the paper asks the reader to buy a fairly large unified framework without a correspondingly strong improvement profile. For ICLR, that matters, because the contribution needs to be more than “we assembled sensible parts into one system.”

2. **The disentanglement claim is stronger than what the paper actually demonstrates.**  
   Section 3.3 states that disentanglement is encouraged “through both training objectives and architectural design,” but the mechanism is weak. Architecturally separating a sequence-valued content code \(\mathbf{z}_c\) from a global style vector \(\mathbf{z}_s\) does not by itself imply disentanglement, and the training objective in **Equation (6)** does not contain an explicit independence penalty, adversarial objective, information bottleneck decomposition, cross-reconstruction constraint, or mutual-information control between content and style. In other words, the paper largely relies on task structure plus a VAE-style prior on \(\mathbf{z}_s\). That is a reasonable heuristic, but it is not enough to support strong disentanglement language.  
   The evidence in **Table 4** actually shows that \(\mathbf{z}_s\) retains substantial composer information, and even the authors acknowledge that composer traits are dominant. This is musically plausible, but it complicates the claimed content-style factorization. If style embeddings strongly encode composer identity, then “style” here is not cleanly separated from composition-level attributes. The paper should either narrow its claim to partial factorization or provide stronger tests showing invariance of \(\mathbf{z}_c\) under performer/style changes and controlled dependence of \(\mathbf{z}_s\).

3. **Several mathematical and objective definitions are underspecified, and this matters because the paper's central claims depend on those details.**  
   The issue starts around **Equations (3) and (4)**. The paper writes both APT and EPR losses as simple cross-entropies,
   \[
   \mathcal{L}_{\mathrm{EPR}} = \mathrm{CE}(\hat{\mathbf{y}}, \mathbf{y}), \qquad
   \mathcal{L}_{\mathrm{APT}} = \mathrm{CE}(\hat{\mathbf{x}}, \mathbf{x}),
   \]
   but the outputs are structured sequences with multiple token types, unequal lengths, and, in the score case, parallel symbolic attributes. It is not clear in the main paper whether \(\mathrm{CE}\) denotes token-level autoregressive loss over a flattened event sequence, sum of per-attribute losses, masked loss over non-padding positions, or something else. This ambiguity is especially problematic because the input score representation is note-wise attribute-based, while the output performance representation is event-based. The training target spaces are thus heterogeneous, but the notation makes them look symmetric.  
   There is also a mismatch between **Equation (8)** in the main paper and **Equation (12)** in Appendix B.2. The main text states that the diffusion model predicts the added noise \(\epsilon\), whereas the appendix says the implementation uses velocity prediction. Those are not identical parameterizations. The appendix may explain the actual implementation, but the main paper should not present one objective while the appendix describes another.  
   Finally, **Equation (6)** in the main text gives an unweighted sum of losses, while **Equation (11)** in the appendix introduces \(\lambda_{\text{rec}}=0.2\) and \(\lambda_{\text{KL}}=0.1\). Those weights are not minor bookkeeping, they substantially affect training behavior and the claimed disentanglement. The main paper should state the actual optimized objective, not a simplified one that is materially different.

4. **The evaluation of EPR is only partially convincing because the chosen metrics do not cleanly reflect perceptual or stylistic quality, and some comparisons cut in opposite directions.**  
   In **Table 2**, the paper emphasizes variance, KL, and MAE for duration and velocity, but these statistics can be hard to interpret. For instance, matching marginal variance more closely to human data does not necessarily imply better musical phrasing; it can also reflect noisier outputs. The paper says this explicitly when criticizing DExter, which is fair, but then the same caveat should apply more generally to the entire metric suite.  
   **Table 3** is even more puzzling. The score-only baseline has very strong alignment and missing-rate numbers, and **Ours (Target)** is not clearly the best on these accuracy-style metrics. This creates a tension between “human-like expressiveness” and “structural faithfulness,” but the paper does not unpack that trade-off carefully. A stronger analysis would correlate subjective preference with these objective metrics, or at least explain why the metrics should be trusted for comparing systems with very different generation mechanisms.  
   The subjective study in **Figure 2** is directionally positive, but it is based on only eleven trained participants and five pieces. That is not meaningless, but it is a small study for making strong claims about general rendering quality across styles and composers.

5. **The PSR module is interesting, but its evaluation is weaker than the core joint model evaluation.**  
   The paper claims PSR generates “stylistically appropriate” embeddings from score content alone, yet the evidence is mostly visual and indirect. **Figure 4** shows 2D projections where PSR-generated style embeddings approximately follow the same era-wise arrangement as extracted real-performance embeddings, but 2D projections are notoriously fragile and classifier-dependent. Similar-looking clusters in 2D are not strong evidence that the full distributions match in the original latent space.  
   Moreover, the paper uses era labels inferred from metadata parsing, then projects embeddings through a classifier bottleneck from Section 5.2. That makes the evaluation pipeline fairly indirect. If the claim is that PSR captures appropriate style distributions conditioned on score content, I would expect stronger quantitative tests, for example retrieval of human styles conditioned on similar scores, likelihood or distance measures in latent space, or blinded pairwise judgments comparing target-style, PSR-style, and random-style renderings. As presented, PSR looks promising, but the evidential bar is lower than the paper suggests.

6. **The paper's treatment of unpaired data is not fully convincing because the unpaired performance source introduces a confound that is acknowledged but not really resolved.**  
   In Section 4.1 and Appendix E, the unpaired performance dataset is built from YouTube piano cover videos transcribed into MIDI by an audio-to-MIDI system. The paper openly notes possible transcription artifacts and quantization biases. That is important because the style encoder and the joint model may then partly learn properties of the transcription system rather than purely human expressive style. Since the paper also argues that unpaired data improves style representation, this confound matters directly to one of the central conclusions.  
   The ablation in **Table 12** shows that more unpaired data helps APT, and **Table 13** suggests improvements in style-based identification, but neither result separates “more diverse musical signal” from “more exposure to the biases of a fixed transcription pipeline.” Without at least some robustness check using cleaner held-out performances, it is hard to know how much of the gain is musically meaningful.

7. **The paper claims practical score transcription ability, but the evidence for notation quality is weaker than the headline APT numbers suggest.**  
   The APT metrics in **Table 1** include notation-oriented measures, which is good, but the qualitative score examples in **Figure 9-Figure 11** suggest that the outputs can still contain readability and notation-structure issues. This matters because symbolic-to-score transcription is not only about note recovery, it is also about producing musically readable notation. The main text does not analyze these examples in detail, and the reader is left to infer how often the system makes formatting or voice-structure mistakes that are not well captured by average edit metrics.  
   More broadly, the paper leans on “competitive APT” as support for the unified content representation, but if the output is still weak on practical notation quality, that weakens the translational value of the joint framework.

8. **Some baselines and comparisons are not as strong as they could be, especially on the EPR side.**  
   The paper compares mainly to VirtuosoNet and DExter for EPR. These are relevant, but given the pace of symbolic music generation and performance rendering, the baseline suite still feels somewhat narrow for such a broad claim about competitive EPR. Also, since **Figure 1** and the overall narrative center the joint nature of the model, it would have been helpful to include stronger decomposition ablations: for example, joint model without masked reconstruction, joint model without KL, joint model with random or averaged style, joint model with shared versus separate encoders, and PSR conditioned on weaker score summaries. The appendix offers some ablations, but the main paper does not surface the ones most needed to justify the architecture.

9. **Presentation is generally decent, but there are enough inconsistencies and notation issues that they start to affect technical confidence.**  
   There are small but recurring mismatches, for example \(E_{\text{const}}\) versus \(E_{\text{struct}}\), \(E_{\text{das}}\)/\(E_{\text{dut}}\), and irregular notation for score-content variables \(\mathbf{z}_x\), \(\mathbf{z}_y\), and \(\mathbf{z}_c\). These are not fatal individually, but in a paper that already relies on several representation conversions and training objectives, such inconsistencies make it harder to verify exactly what is being optimized and evaluated.

## Questions
1. The main paper's training objective in **Equation (6)** is an unweighted sum, while Appendix B gives the actual weighted objective in **Equation (11)** with \(\lambda_{\text{rec}}=0.2\) and \(\lambda_{\text{KL}}=0.1\). Which objective was actually used for all reported experiments, and can the authors provide an ablation showing sensitivity to these weights in the main results, not just the KL-weight analysis in Table 14?

2. For **Equations (3) and (4)**, please specify exactly how \(\mathrm{CE}\) is computed for each task. Is the score decoder predicting flattened autoregressive tokens, or parallel note attributes? How are padding and multi-field outputs handled? A concise but precise definition would improve reproducibility and confidence.

3. The PSR objective in the main text predicts \(\epsilon\), while Appendix B.2 says the implementation uses velocity prediction. Please clarify which parameterization is used in the final model and whether the reported PSR results are sensitive to this choice.

4. Can the authors provide a stronger disentanglement test beyond classification and 2D visualization? For example, if the same score has multiple performances, how invariant is \(\mathbf{z}_c\) across performers, and how much does \(\mathbf{z}_s\) vary? A quantitative within-piece / across-piece analysis would substantially increase my confidence.

5. In **Table 3**, the score-only baseline is quite strong on alignment-like metrics, and **Ours (Target)** is not uniformly best. Can the authors explain more clearly what failure modes these metrics capture and why higher perceptual quality in **Figure 2** should outweigh weaker structural-faithfulness numbers in some cases?

6. Since the unpaired performance data comes from audio transcriptions of YouTube videos, do the authors have any estimate of how much transcription noise affects the learned style space? Even a small controlled study on a clean subset would help.

7. The qualitative APT examples in **Figure 9-Figure 11** are useful, but can the authors quantify notation-readability errors more directly, especially time signature, voice assignment, or beaming/stem issues if applicable? This would strengthen the practical relevance of the APT side.

## Flag For Ethics Review
- Yes, Privacy, security and safety  
- Yes, Legal compliance (e.g., GDPR, copyright, terms of use)  
- Yes, Responsible research practice (e.g., human subjects, data release)

## Details Of Ethics Concerns
The concerns are moderate rather than severe, but they should be acknowledged.

First, the unpaired performance dataset is compiled from **YouTube piano cover videos** (Section 4.1). The paper does not discuss licensing, terms-of-use compliance, or whether the resulting transcribed MIDI data can be redistributed. Since the data source is platform-hosted user content, legal and copyright status should be clarified.

Second, although the human listening study is described as low risk and voluntary in the ethics statement, the main paper gives only limited procedural detail. It would help to state compensation, recruitment conditions, and whether institutional approval was required or exempted.

Third, because the pipeline uses an automatic transcription model to convert public performances into MIDI, there is a risk that artifacts from this model become encoded in the learned style representation. This is less an ethics violation than a responsible research practice issue, because the provenance and noise properties of the unpaired data affect the validity of the conclusions.

## Soundness Rating
2: fair. The paper is technically plausible and supported by a substantial experimental section, but several central claims, especially around disentanglement and PSR effectiveness, are backed by weaker evidence than the narrative suggests, and some objective definitions are underspecified.

## Presentation Rating
3: good. The paper is generally readable and well organized, with useful figures and a broad empirical section, but there are enough inconsistencies between equations, notation, and implementation descriptions to reduce clarity.

## Contribution Rating
2: fair. The joint formulation is interesting and useful, but the methodological novelty is limited, and the empirical gains do not consistently justify the breadth of the claims.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted. The paper is thoughtful, technically competent, and clearly relevant, but for me it falls short of ICLR standard mainly because the novelty is modest, the disentanglement story is only partially substantiated, and several core methodological details and evaluation choices need tightening.

## Reviewer Confidence
4: confident. I am confident in this assessment, though not absolutely certain. The topic is close to my expertise, and I checked the methodology, tables, equations, and figures carefully, but some implementation details are still ambiguous in the main paper.