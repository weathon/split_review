---
job_id: a50a3aeb-b681-49b3-84ae-6a6f610c94a0
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: 1CR1MTIgmq.pdf
paper: False, Misleading, and Unfounded Statements in a Recent TPAMI Publication
main_score_norm: 0.2
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is about EEG-based machine learning evaluation, dataset confounds, and the validity of claims in neural decoding, which falls within ML applications to neuroscience/cognitive science and broader questions of dataset validity and empirical methodology.

## Minimum Quality
Pass ✅. Although this is not a standard methods paper and is framed as a critique/refutation, it contains the core elements needed to assess it on its own terms, namely an abstract, introduction, claim-by-claim analysis, one new empirical analysis with a figure and results table, and a conclusion. The paper is clearly written in English and is complete enough to review, even though several aspects fall well short of ICLR standards.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden prompts, invisible text, or instructions aimed at manipulating automated reviewers in the provided paper content.

# Expected Review Outcome:
## Summary
This submission is a critique-focused paper that disputes a recent TPAMI response by Palazzo et al. (2024) concerning EEG-based visual decoding, especially around temporal confounds, interleaved versus block designs, subject attentiveness, session duration, cross-subject variability, and the use of supertrials. In addition to textual rebuttal, the paper includes one new empirical analysis on frequency-domain supertrial averaging over the Ahmed et al. (2021) dataset, summarized in **Figure 1** and **Table 1**, to argue that supertrials do not necessarily suppress higher-frequency information and that the main conclusions of Bharadwaj et al. (2023) still hold.

## Strengths
The paper addresses an important issue for the community, namely whether widely used EEG decoding protocols are confounded and whether published counterarguments to that claim are themselves valid. Even if one disagrees with parts of the framing, there is genuine scientific value in scrutinizing data collection protocols and evaluation logic, especially in a literature where inflated conclusions can propagate quickly.

The manuscript is unusually explicit about the exact claims it is contesting. The structure is easy to follow because each section isolates a specific disputed point, cites the quoted claim, and then provides a point-by-point response. For a critique paper, that directness is useful.

The one piece of new empirical evidence, while limited, is at least concretely tied to one of the central disputed claims. In particular, **Figure 1** is helpful because it directly visualizes how average spectra change as supertrial size \(N\) increases under the authors’ frequency-domain averaging procedure. Whether or not one accepts the broader interpretation, the figure does engage the claim that supertrials must attenuate higher frequencies, and it does so in a way that is more informative than purely verbal argument.

Similarly, **Table 1** is relevant to the paper’s stated objective. It does not just present one aggregate number, it reports per-model accuracies across multiple supertrial sizes \(N\), which allows the reader to see that the claimed failure mode is model-dependent rather than universal. The pattern in **Table 1**, where EEGChannelNet stays around chance while EEGNet, 1D CNN, SVM, and sometimes SyncNet are above chance for some \(N\), is at least consistent with the narrow conclusion that the frequency-domain supertrial construction does not rescue EEGChannelNet.

The paper also makes reproducibility gestures by naming the underlying dataset and stating that code will be released. For a refutation-style paper, that is appreciated.

## Weaknesses
1. **The paper is framed much more as a prosecutorial rebuttal than as a scientific contribution suitable for the ICLR main track.**  
   The title, abstract, and repeated wording throughout the paper lean heavily on charged assertions such as “false,” “misleading,” “invalid,” “unfounded,” and “debunks nearly one hundred published papers” (**Abstract; Pages 1, 9, 10, 11**). A critique paper can absolutely be sharp, but here the rhetoric often outruns the analysis. The manuscript spends much more effort asserting that another paper is wrong than extracting a generalizable methodological lesson, formal diagnostic, benchmark, or protocol that the ICLR community can adopt. As submitted, this reads closer to a discipline-specific rejoinder or commentary than to a research paper that advances ML methodology, theory, or benchmarking in a reusable way.

2. **The central evidence base is too thin relative to the scope and confidence of the claims.**  
   The paper makes very broad claims about the invalidity of arguments made in Palazzo et al. (2024), and at the end broadens this to claims about “nearly one hundred papers” and “seventeen datasets” (**Pages 9 to 11**). Yet the new evidence introduced in this manuscript is essentially one analysis on one dataset, one preprocessing variant, one figure, and one results table (**Section 7, Figure 1, Table 1**). That mismatch matters. If the goal is to convince a broad ML audience, the paper needs either a much more systematic empirical study across datasets/protocols, or a more careful narrowing of claims. Right now the manuscript asks the reader to accept very expansive conclusions from a very narrow new experiment plus extensive quotation-based argumentation.

3. **The new experimental analysis in Section 7 is underspecified in ways that directly affect its validity.**  
   The paper states, on **Page 4**, that it “perform[s] an FFT on each sample, averag[es] the magnitude and phase of the samples independently, and perform[s] an inverse FFT on the average.” This is not a small implementation detail, it is the core operation being used to dispute the frequency-attenuation claim. But the method is mathematically ambiguous:
   - How is phase averaged, exactly? Arithmetic averaging of wrapped angles is generally invalid because of circularity. Averaging phases \(\phi_i\) should use a circular mean such as  
     \[
     \bar{\phi} = \operatorname{atan2}\!\left(\frac{1}{N}\sum_i \sin \phi_i,\; \frac{1}{N}\sum_i \cos \phi_i\right),
     \]
     not a plain linear mean over \([-\pi,\pi)\).
   - If the method instead averages complex Fourier coefficients, that is a different operation than independently averaging magnitude and phase.
   - It is also unclear whether the FFT is applied to raw signals, windowed signals, or filtered signals, and whether any normalization is used before inverse FFT.
   
   Without this level of specification, the key empirical claim in **Figure 1** is hard to interpret or reproduce. This is exactly the sort of signal-processing detail that can qualitatively change spectral behavior.

4. **The statistical testing around Table 1 is not convincing enough for the number of comparisons being made.**  
   **Table 1** reports \(11\) supertrial sizes across \(8\) models, so \(88\) hypothesis checks are implicitly being presented, with starred values declared significant at \(p<0.005\) via “a binomial cmf” (**Page 5**). This raises several issues:
   - The paper does not specify the exact null hypothesis, the number of test samples used for each \(N\), or whether one-sided or two-sided tests were used.
   - No correction for multiple comparisons is described, despite the large number of model-\(N\) combinations tested.
   - The binomial model assumes independent Bernoulli trials, but supertrial construction and fold-based evaluation can induce dependencies between test samples, especially if original trials are reused across folds or grouped deterministically.
   
   This matters because many of the “significant” gains are numerically small, for example **SyncNet at \(N=4\)** is only **3.7%** versus **2.5%** chance, and several starred entries are barely above chance. With better-controlled inference, some of these claims may weaken materially.

5. **Figure 1 does not actually establish the conclusion the authors want it to establish.**  
   The paper says, “It can be seen that this does not attenuate higher-frequency components. In fact, it amplifies them” (**Page 4**). That is too strong given what the figure shows. **Figure 1** plots average spectra in dB after frequency-domain averaging, but a change in average spectral magnitude does not by itself demonstrate preservation of discriminative high-frequency neural information. An increase in average high-frequency power could also come from artifacts of the averaging procedure, scaling conventions, phase handling, or noise structure. The figure is useful descriptively, but it does not support the stronger inferential leap from “spectrum changed this way” to “therefore the prior criticism is invalid.” At minimum, the paper should connect spectral observations to class-separability metrics or per-band decoding analyses.

6. **The empirical results in Table 1 are themselves mixed, and the paper overstates what they show.**  
   The authors present **Table 1** as validating the original claim of Bharadwaj et al. (2023), but the table is not uniformly supportive. Several methods degrade back toward chance as \(N\) grows; for instance, **1D CNN** falls from **7.5% at \(N=5\)** to **2.3% at \(N=20\)** and then remains around chance, while **EEGNet** also drops substantially for larger \(N\). So the evidence is not “supertrials work” in any robust sense, but rather “some models are above chance for some intermediate \(N\).” That is a much narrower and less stable conclusion. The manuscript should say that plainly instead of presenting the table as a broad vindication.

7. **Much of the paper’s argumentation hinges on textual interpretation and rhetoric rather than controlled analysis.**  
   Many sections, especially **Sections 2, 3, 4, 5, 6, and 8**, proceed by quoting statements from prior work and then declaring them “unfounded,” “misleading,” or “false.” Sometimes the rebuttal is reasonable, but often the evidentiary standard is asymmetric. For example, in **Section 2** the authors argue that a 1 s blank is “likely to preclude significant signal bleeding,” but that is still a conjectural statement unless directly quantified in the dataset at issue. In **Section 3**, they infer attentiveness partly from above-chance classification accuracy, but that is not a clean proxy for attentiveness without excluding other structured cues or biases. The manuscript repeatedly demands strict proof from the opposing side while permitting itself looser inferential steps.

8. **The paper does not sufficiently separate “not a confound” from “not a problem for decoding.”**  
   In **Section 8** on **Pages 6 to 9**, the manuscript argues that certain issues raised by Palazzo et al. are not “confounds” under a specific definition and therefore their use of the term is false. This is partly semantic. Even if one grants the definitional point, practical issues like carryover responses, attentional drift, session fatigue, or altered saliency can still invalidate interpretations of decoding performance. The paper spends substantial effort litigating terminology rather than clarifying which design factors bias class-decoding estimates upward, which bias them downward, and which mainly affect interpretability. For an ML audience, that taxonomy would be much more valuable than a dictionary-style dispute.

9. **The positioning relative to prior work is incomplete and not sufficiently synthetic.**  
   The manuscript cites a very large number of papers, but mostly to classify them as flawed or implicated. What is missing is a balanced related-work synthesis of refutation-style studies, modern non-confounded EEG decoding benchmarks, and broader methodology for identifying temporal leakage/confounds. In particular, the paper would benefit from a more structured positioning against prior commentaries and surveys of EEG visual decoding, rather than largely centering one adversarial exchange. As written, the literature discussion feels like dossier-building, not scholarly synthesis.

10. **The presentation, while readable sentence-to-sentence, is not professional enough in tone for archival publication.**  
    This is not just a stylistic complaint. Statements like “a systemic flaw of the entire peer review process across an entire field of inquiry” and repeated accusations across dozens of papers (**Pages 10 to 11**) substantially raise the burden of evidence and neutral framing. A strong refutation should let the data and logic do the work. Here the paper often sounds like it wants to win a dispute rather than persuade a critical reader. That weakens credibility, even in places where the authors may be substantively correct.

11. **The paper’s contribution is too narrow for ICLR unless it is turned into a broader benchmark/protocol paper.**  
    A useful ICLR version of this work would likely need one of the following: a standardized confound-detection benchmark across multiple EEG datasets, a formal taxonomy of temporal leakage modes with recommended evaluation protocols, a reproducible toolkit for diagnosing block/interleaved confounds, or a comprehensive replication study. In its current form, the paper is mostly a targeted rebuttal plus one extra experiment. That may have value in a commentary venue, but it is not enough here.

## Questions
1. The core new methodological step in **Section 7** needs to be defined much more precisely. How exactly is phase averaged in the Fourier domain? Is it a circular mean over angles, averaging of complex coefficients, or something else? Please provide the exact formula and preprocessing pipeline. A precise answer here would materially increase my confidence in the interpretation of **Figure 1**.

2. For the significance stars in **Table 1**, please state the exact test sample counts for each \(N\), the exact null model, whether trials/supertrials are independent under your evaluation pipeline, and whether you applied any correction for the \(88\) comparisons shown. If not, can you provide corrected significance results? This could change my view of how strong the evidence in the table really is.

3. Can you provide a band-specific decoding analysis, rather than only average spectral plots in **Figure 1**? Right now the figure shows changes in mean spectrum, but not whether high-frequency information remains discriminative. A per-band or band-ablation decoding comparison would be much stronger evidence for the claim you make in **Section 7**.

4. Several sections rely on language such as “likely,” “we have no reason to believe,” or “would not be possible” when contesting prior claims, especially in **Sections 2, 3, and 8**. Can you more clearly separate direct empirical evidence from inference and opinion? That would improve both soundness and tone.

5. The manuscript would be more compelling if it generalized beyond a single dispute. Can you articulate the reusable methodological takeaway for the broader ML community? For example, what concrete protocol, evaluation checklist, or benchmark should future EEG decoding papers adopt as a result of this work?

6. Are there additional experiments on datasets beyond Ahmed et al. (2021) that you can include in the main paper? Given the breadth of the claims, a single-dataset analysis feels insufficient.

## Flag For Ethics Review
- Yes, Responsible research practice (e.g., human subjects, data release)  
- Yes, Unprofessional behaviors (e.g., unprofessional exchange between authors and reviewers)

## Details Of Ethics Concerns
The paper is not raising the usual data privacy or safety issues, but I do have concerns about responsible research practice and professional tone.

First, the manuscript repeatedly describes another paper’s statements as “false,” “misleading,” “invalid,” and “unfounded” throughout the main text, title, and abstract, and extends these accusations to a very large body of work on **Pages 9 to 11**. A refutation paper can and sometimes should be critical, but the current language is stronger and more adversarial than is typical for scientific discourse, especially given that several points are argued from partial evidence rather than direct demonstration.

Second, the manuscript makes sweeping claims about “debunk[ing] nearly one hundred published papers” and failures of “the entire peer review process” (**Pages 9 to 11**). Claims of that breadth require a correspondingly systematic evidentiary basis and careful framing. As written, the presentation risks crossing from scientific critique into unprofessional broad-brush condemnation.

These concerns do not imply misconduct, but they do matter for editorial judgment and for whether the paper models responsible scholarly disagreement.

## Soundness Rating
2: fair. The paper raises legitimate concerns and includes some relevant evidence, but the central new experiment is underspecified, the statistical testing is weakly justified, and several strong conclusions go beyond what is directly shown.

## Presentation Rating
2: fair. The paper is organized and readable, but the tone is overly adversarial, the contribution is not framed in a sufficiently general way for ICLR, and key methodological details in Section 7 are missing.

## Contribution Rating
1: poor. The paper tackles an important issue, but as a main-track ICLR submission the contribution is too narrow and too centered on rebutting a specific prior response, with limited new empirical or methodological substance.

## Overall Rating
2: Reject, not good enough. The topic matters, and some of the critique may be substantively valid, but the submission is not strong enough as an ICLR main-track paper. The new evidence is too limited and underspecified relative to the scope of the claims, the statistical support around Table 1 is not convincing, and the paper reads more like a pointed rejoinder than a broadly useful ML research contribution.

## Reviewer Confidence
4: confident. I am confident in this assessment, though not absolutely certain. The main issues driving my score are about contribution type, evidentiary scope, statistical support, and professional presentation, rather than about obscure domain-specific details.