---
job_id: 94e7f28f-72d9-430d-a581-6b8b49c95160
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: 4S5x8yhJ5H.pdf
paper: Vibeface - Video and Image Biometric Dataset for Evaluation of Faces
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The submission is a dataset-and-benchmark paper for biometric face verification, with relevance to representation learning, computer vision, fairness, privacy, and datasets/benchmarks, all of which are within ICLR scope.

## Minimum Quality
Pass ✅. The paper has the essential structure for a dataset paper, including abstract, introduction, related work, dataset description, benchmark tasks, quantitative results, and conclusion. While the contribution is limited and several methodological details are weak or missing, these issues do not rise to the level of a desk reject.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I found no hidden prompts, suspicious instructions to automated reviewers, or other signs of manipulative content in the provided paper text.

# Expected Review Outcome:
## Summary
This paper introduces VIBEFACE, a facial biometric dataset intended for evaluation of face verification systems in eKYC-like settings. The dataset contains 2,250 still images and 1,550 short videos from 50 subjects, with acquisition organized across multiple sessions varying lighting, glasses, and capture conditions, and the paper provides baseline benchmarks for face detection and face verification using standard off-the-shelf models.

## Strengths
The paper addresses a practically relevant gap. The focus on eKYC-style video capture is useful, since many face datasets emphasize either still images or controlled videos rather than the kinds of short interaction sequences described in Section 3.2, such as blinking, head movement, and partial occlusion. This makes the proposed collection more operationally grounded than many standard face datasets.

The paper also puts visible effort into responsible data collection. Section 3.4 and Section 3.5 clearly describe informed consent, controlled access, non-commercial use, and anonymized identifiers. For a biometric dataset paper, this is not a minor detail, and it is good to see the authors treating licensing and consent as part of the contribution rather than an afterthought.

The acquisition protocol is reasonably well organized. The distinction between standardized photos, selfie photos, selfie videos, and verification videos in Section 3.2 is easy to follow, and Table 2 gives a concise overview of which scenarios appear in which sessions. That table is one of the stronger presentation elements in the paper because it makes the structure of the dataset substantially easier to understand than the prose alone.

Figure 2 is helpful for concretizing the photo scenarios. It shows that the dataset does include both operator-captured pose variation and user-captured selfie variation, rather than just relabeling a standard mugshot setup as “in the wild.” Likewise, Figure 3 helps clarify what the authors mean by eKYC-style verification sequences, especially the motion-based prompts. These figures do useful explanatory work and are well aligned with the paper’s central claim about operational realism.

The benchmark section, while limited, at least provides a sanity check that the dataset is nontrivial. In Table 3, MTCNN degrades noticeably under eyeglasses and weak lighting, whereas RetinaFace is nearly saturated. In Table 4, frontal-view verification is easy, but off-angle views and some motion scenarios are much harder, especially for MagFace. This pattern supports the claim that the dataset contains some meaningful nuisance variation rather than being entirely trivial.

## Weaknesses
1. **The dataset is simply too small to support many of the claims about benchmarking, robustness, and fairness.**  
   The paper repeatedly frames VIBEFACE as a “comprehensive,” “demographically rich,” and “new benchmark” resource, but the actual scale is 50 subjects total, as stated in Section 3.1. For a face verification dataset, especially one making demographic claims across gender, age, and four racial categories, this is very limited. Once the data are broken down by session, scenario, age bin, gender, and race, the effective sample sizes become tiny. This matters because the paper goes beyond describing the dataset and starts interpreting subgroup differences as meaningful findings. With only 12 to 13 subjects per racial category and a total of 50 identities, the evidence is far too thin to support robust conclusions about fairness or demographic performance trends.

2. **The novelty claim is overstated and the positioning against prior datasets is incomplete.**  
   The central claim is that there are no publicly available datasets with authentic eKYC-style facial videos alongside still images. That is a strong positioning statement, yet the related work in Section 2 is narrow and mostly compares against older mobile biometrics or anti-spoofing datasets. The comparison in Table 1 is also selective and somewhat favorable to the proposed dataset. For example, the paper does not sufficiently engage with more recent selfie-focused and eKYC-adjacent datasets, nor does it disentangle whether the actual novelty is “first eKYC dataset,” “first controlled-access ethically sourced eKYC dataset,” or simply “a small dataset with eKYC-inspired prompts.” Those are very different claims. As written, the positioning feels more like marketing than careful scholarship.

3. **The benchmark design is too weak to establish VIBEFACE as a meaningful evaluation benchmark.**  
   The benchmark tasks in Section 4 are very minimal: three standard detectors and two standard face recognition models, all used off the shelf. There is no training protocol, no cross-dataset transfer experiment, no fine-tuning study, no leave-one-session-out evaluation, no cross-device generalization, and no comparison showing that models rank differently on VIBEFACE than on existing datasets. As a result, the benchmark section reads more like a dataset sanity check than a serious benchmark contribution.  
   This matters because the paper repeatedly claims to “establish a new benchmark,” but benchmarking is not just releasing data and running ArcFace/MagFace once. It requires a clearly defined task protocol, carefully justified metrics, and enough experimental depth to show that the benchmark reveals something scientifically useful.

4. **The face verification evaluation protocol is underspecified and arguably not appropriate for the claims being made.**  
   In Section 4.2, verification is considered successful when the similarity score exceeds a fixed threshold of 0.5, and performance is measured as the percentage of frames correctly authenticated. This is a particularly weak protocol for a biometric verification paper. There is no explanation of how the threshold 0.5 was selected, whether it is model-specific, whether embeddings were normalized, whether cosine similarity or another score was used, and whether this threshold corresponds to any meaningful operating point such as equal error rate or fixed false accept rate.  
   This is not a nitpick. In biometrics, conclusions are highly sensitive to the operating threshold. Reporting only “percentage above 0.5” makes the results in Table 4 hard to interpret and very hard to compare against prior work. At minimum, the paper should report ROC/DET-style operating characteristics, TAR at fixed FAR, or EER, and specify the exact scoring function \(s(x_{\text{ref}}, x_{\text{query}})\). Without this, the verification benchmark is methodologically weak.

5. **The paper does not define genuine and impostor protocols clearly enough.**  
   Section 4.2 says that a frontal image from Session B is used as the reference sample and that query samples are the same images and videos used in detection. But it is unclear whether evaluation includes only genuine matches for each subject, or both genuine and impostor comparisons. The wording “correctly authenticated” suggests a binary decision setting, yet the paper never specifies how many negative pairs are formed, how impostors are sampled, or whether thresholds were calibrated on held-out data.  
   This is a major omission, not a presentation quibble. Verification performance without a well-defined impostor set is incomplete, and the reported percentages in Table 4 can be misleading if they reflect only true-match acceptance. A face verification paper cannot rely on an implicit metric here.

6. **The fairness analysis is too shallow and statistically ungrounded.**  
   The paper repeatedly emphasizes demographic balance and fairness, but the actual analysis in Tables 3 and 4 is limited to reporting averages over groups. There are no confidence intervals, no hypothesis tests, no variance estimates, and no discussion of whether the observed subgroup gaps are meaningful relative to sample size. For example, on Page 9 the authors note that both models performed slightly worse on the Caucasian subgroup and that the youngest age group yielded the lowest performance, but nothing in the paper quantifies uncertainty around these claims.  
   This matters because the fairness framing is a major part of the motivation. With only 50 participants, a fairness discussion based solely on point estimates risks overinterpretation. If the authors want fairness to be central, they need a more careful statistical treatment or a much larger subject pool.

7. **Table 1 is not very rigorous as a comparative positioning device.**  
   Table 1 presents a high-level comparison across datasets using binary indicators such as eKYC, glasses, demographic data, gender balance, race balance, and age balance. This is a convenient summary, but it is too coarse to support the strong positioning in Section 2. Several columns collapse nuanced properties into yes/no labels, and the criteria for calling a dataset “balanced” are not operationalized. For example, “AB” and “RB” are especially ambiguous. What quantitative threshold defines balance? Does balance refer to enrolled identities, media instances, or both?  
   Since the paper’s novelty claim leans heavily on Table 1, the lack of precise criteria weakens the contribution.

8. **The paper overstates realism, while the acquisition appears substantially controlled.**  
   The introduction motivates unconstrained eKYC settings, “at home,” under heterogeneous mobile devices and natural behaviors. But Section 3 says acquisition was conducted in a controlled studio environment, each session in a separate room, with standardized instructions and supervision by trained operators. This is not inherently bad, but it is not the same thing as true in-the-wild eKYC capture.  
   Figure 2 reinforces this tension. The sample images show clear scenario variation, but they also visually suggest a structured collection setup rather than natural consumer capture. So the paper is caught in an awkward middle ground: more realistic than tightly controlled mugshot datasets, but less realistic than truly unconstrained remote onboarding data. The paper should present this more honestly.

9. **There are missing or inconsistent details in the quantitative tables.**  
   Table 3’s race-category columns appear to list Afr., Cauc., and EA in the visible header, while Section 3.1 states four racial categories including South Asian. By contrast, Table 4 clearly includes SA. This kind of inconsistency is not catastrophic, but it creates avoidable confusion in a paper where demographic analysis is central.  
   More broadly, both tables report many decimal values but no counts, no uncertainty, and no indication of how many frames per scenario/group contribute to each number. Given that video scenarios are sampled at 6 fps, the frame-level aggregation can substantially inflate apparent sample size relative to the number of identities. The paper should make this explicit.

10. **The benchmark results are not especially informative scientifically.**  
   Looking at Table 3, RetinaFace is essentially perfect in most settings, including all frontal and many off-angle conditions. That tells me either the detection task is too easy for modern detectors or the metric is too coarse to reveal difficulty. Similarly, Table 4 shows frontal-view verification at or near 1.0 for both ArcFace and MagFace, while off-angle views collapse toward roughly 0.26 to 0.51 depending on the model. This pattern is directionally plausible, but the paper does not probe *why* these failures occur, whether they are due to pose, crop quality, score calibration, motion blur, or reference mismatch.  
   A benchmark paper should extract more insight than “easy settings are easy, harder settings are harder.”

11. **The dataset utility claims in the conclusion extend beyond what is demonstrated.**  
   In Section 5 the paper suggests the dataset is well-suited for presentation attack detection and deepfake injection attack research. But the dataset, as described in the main paper, contains bona fide samples only. There are no attack samples, no manipulated videos, and no experiments supporting PAD or deepfake-detection use. It is reasonable to say the dataset might serve as bona fide material in larger pipelines, but the current wording overreaches beyond the demonstrated scope.

12. **Presentation is decent overall, but several claims would benefit from more precise formalization.**  
   This paper has almost no mathematical content, which is acceptable for a dataset paper, but then the task definitions and metrics must be especially precise. Instead, several core quantities are left informal. For face detection, “percentage of frames in which a face was successfully detected” needs a stricter criterion, for example whether any detected box counts, whether multiple faces are possible, and what IoU threshold is required relative to annotation. For face verification, the scoring rule should be written explicitly, e.g. \(s(f(x_r), f(x_q)) > \tau\) with a defined embedding function \(f\), similarity \(s\), and threshold \(\tau\). Without that level of formalization, the paper’s empirical section feels under-specified.

## Questions
1. In Section 4.2, what exactly is the verification protocol? Please state explicitly whether the evaluation includes both genuine and impostor comparisons. If impostors are included, how are negative pairs constructed, and in what quantity?

2. Why was the threshold fixed at \(0.5\) for both ArcFace and MagFace? Was this chosen from prior documentation, tuned on held-out data, or set ad hoc? A convincing rebuttal would ideally include threshold-free metrics such as ROC, EER, or TAR at fixed FAR.

3. What similarity function is used in verification, cosine similarity or something else? Are embeddings normalized before scoring? This should be stated explicitly because the interpretation of the \(0.5\) threshold depends on it.

4. For Table 3, what exactly counts as a successful face detection? Is there ground-truth annotation and an IoU threshold, or is detection counted whenever the model outputs any face box? If the latter, the metric is too loose for a benchmark paper.

5. Can the authors provide counts or uncertainty estimates for the subgroup analyses in Tables 3 and 4? Since the paper makes demographic claims, confidence intervals or subject-level aggregation would materially increase confidence in the conclusions.

6. Please clarify the discrepancy in demographic reporting across the race-category columns in Table 3 versus the four race groups described in Section 3.1.

7. Can the authors better situate the realism claim? The paper motivates unconstrained eKYC usage, but Section 3 describes supervised studio collection. I would like the authors to be more precise about which aspects are realistic, device diversity, action prompts, selfie posture, and lighting variation, versus which aspects remain controlled.

8. The paper says VIBEFACE is a “benchmark.” What experimental protocol do the authors envision as the canonical one for future use, beyond the simple off-the-shelf baselines in Section 4? A clearer benchmark definition would strengthen the paper substantially.

## Flag For Ethics Review
- Yes, Privacy, security and safety  
- Yes, Legal compliance (e.g., GDPR, copyright, terms of use)  
- Yes, Potentially harmful insights, methodologies and applications  

## Details Of Ethics Concerns
The paper describes a dataset of facial biometric images and videos from consenting adults, so this is not an ethics red flag in the sense of obvious misconduct. However, biometric face datasets inherently raise privacy, misuse, and dual-use concerns. Section 3.4 and Section 3.5 acknowledge controlled access, non-commercial use, anonymized identifiers, and GDPR-oriented consent, which is good, but these measures do not eliminate the underlying risk that facial biometric data can be repurposed for surveillance, re-identification, or security-sensitive deployment.

There is also a legal/compliance angle because the paper explicitly invokes GDPR and the EU AI Act in Section 3.4. Since the dataset is intended for biometric applications, the conditions of access, subject withdrawal, and downstream use restrictions are central and deserve careful scrutiny by the venue.

Finally, the work is directly tied to identity verification and eKYC workflows, which are high-stakes settings. Even though the paper presents the dataset as a research resource, the associated methods can be used in systems with exclusionary or surveillance consequences, especially if fairness claims are overstated from a very small sample.

## Soundness Rating
2: fair. The dataset description is mostly coherent and the benchmark experiments are plausible as sanity checks, but the central empirical claims are only partially supported because the verification protocol is underspecified, the fairness analysis is weak, and the benchmark methodology is too limited.

## Presentation Rating
3: good. The paper is generally readable, the dataset structure is understandable, and figures/tables such as Figure 2, Figure 3, and Table 2 are useful. However, several central definitions and evaluation details are missing or too informal, which prevents a higher score.

## Contribution Rating
2: fair. The eKYC-oriented data collection angle is relevant, but the small scale, limited benchmarking, and overstated novelty/benchmark claims keep the overall contribution below what I would expect for ICLR main track.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted. The paper has a useful applied dataset idea and responsible collection practices, but in its current form it does not convincingly establish itself as a strong benchmark contribution for ICLR. The small scale, weakly specified verification protocol, limited experimental depth, and overextended fairness/novelty claims collectively push me below the bar.

## Reviewer Confidence
4: confident. I am confident in this assessment, though not absolutely certain. The paper is straightforward to evaluate as a dataset/benchmark submission, and the main concerns are concrete and directly grounded in the provided text and tables.