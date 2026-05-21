---
job_id: 1165aa98-9e7a-4528-a2c1-13b00929ce83
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: W4FAenIrQ2.pdf
paper: REDSAGE: A Cybersecurity Generalist LLM
main_score_norm: 0.6
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope through domain-specialized LLM training, continual pretraining, post-training, benchmarking, evaluation methodology, and safety/privacy considerations for ML systems.

## Minimum Quality
Pass ✅. The paper contains the expected research structure, including Abstract, Introduction, Related Work, Method, Experiments, quantitative and qualitative Results, Discussion/Limitations, and Conclusion; it presents substantial empirical evidence and is written in clear scientific English, despite several methodological gaps that affect confidence in some claims.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden prompts, suspicious instructions to automated reviewers, or other manipulative content in the provided paper text and figures.

# Expected Review Outcome:
## Summary
This paper presents RedSage, an open 8B cybersecurity-focused LLM built from a multi-stage pipeline consisting of cybersecurity continual pretraining on a large filtered corpus, supervised fine-tuning on agentically generated multi-turn conversations, and DPO alignment. The paper also introduces RedSage-Bench, a new benchmark spanning cybersecurity knowledge, skills, and tool proficiency, and reports results on both the proposed benchmark and several existing cybersecurity and general-language benchmarks.

## Strengths
The paper is ambitious and unusually complete for a domain-specialized LLM submission. It does not stop at "we fine-tuned a base model and got a few gains", but instead covers the full stack: corpus construction, augmentation, model training, benchmark construction, and broad empirical evaluation. That end-to-end framing is one of the strongest aspects of the work.

The data contribution is substantial. The authors curate multiple complementary resources, including CyberFineWeb for domain-adaptive pretraining, RedSage-Seed for higher-quality curated resources, RedSage-Conv for post-training, and RedSage-Bench for evaluation. Even if one disagrees with some design choices, this is materially more useful to the community than yet another closed security model paper. Table 2, on Page 3, makes this point effectively by contrasting RedSage with prior cybersecurity-tuned LLM efforts in terms of pretraining tokens, SFT scale, agentic augmentation, and openness. The openness angle matters here because much prior work in this space is hard to reproduce.

The pipeline is presented clearly at a high level. Figure 1 on Page 1 and Figure 3 on Page 4 give a coherent overview of how the different datasets and stages connect. Figure 4 on Page 5 is particularly helpful because it goes beyond a box-and-arrow diagram and shows the planner/augmenter decomposition with an example grounded in seed data. That figure supports the paper’s central claim that the authors are not merely reformatting documents into QA pairs, but trying to synthesize task-oriented dialogues aligned with realistic workflows.

The benchmark contribution is meaningful. Table 1 on Page 2 and Figure 2 on Page 2 make a plausible case that existing cybersecurity benchmarks under-cover tool proficiency and do not systematically score free-form answers. RedSage-Bench fills a genuine gap by combining knowledge, skills, and tool usage, and by including both MCQ and open-ended QA. I also appreciated that the benchmark is balanced across categories rather than being dominated by one easy slice.

The empirical section is broad. The paper evaluates on the proposed benchmark, multiple external cybersecurity benchmarks, and general benchmarks. This is important because domain-tuning papers often overfit their own evaluation story. Table 5 on Page 9 is especially strong evidence that the gains are not confined to RedSage-Bench. The improvement over Qwen3-8B and several cybersecurity baselines across CTI-Bench, CyberMetric, SECURE, SecEval, and SecBench gives the paper more credibility than a single benchmark win would.

The analysis of different training stages is useful. Table 4 on Page 8 and Table 5 on Page 9 separate CFW-only, Seed-only, and combined pretraining variants, then compare instruction-tuned and DPO versions. That ablation is not exhaustive, but it is enough to support the claim that CyberFineWeb and RedSage-Seed provide complementary benefits. In particular, the CFW vs Seed contrast in Table 5 is informative, rather than decorative.

The generalization story is better than I expected from a security-specialized model. Table 6 on Page 10 shows that the instruction-tuned RedSage variants remain competitive, and sometimes strong, on general benchmarks. I would not overstate this, but it does weaken the common criticism that narrow domain specialization inevitably wrecks broader instruction following.

The qualitative examples are not just fluff. Figure 6 on Page 8 is genuinely informative because it separates correctness from answer quality for the open-ended setting, and the category-wise violin plots show that tool tasks are the hardest. Figures 12 to 15 in the appendix also give a concrete sense of where RedSage helps, especially for exact tool syntax and operational knowledge, where generic models often look impressive until they emit a subtly wrong flag.

The paper is reasonably reproducible by the standards of LLM systems papers. The training pipeline, datasets, prompts, and evaluation setup are described in enough detail that one can understand what was done, even if some implementation details still need tightening.

## Weaknesses
My main concern is that the paper bundles three contributions, model, dataset pipeline, and benchmark, but the validation is still too entangled to cleanly attribute where the gains come from. The benchmark is generated from the same curated seed resources that also feed augmentation and pretraining, and while the authors do perform a semantic-similarity decontamination step on Page 6, this does not fully resolve the more structural concern that train and test are drawn from a closely related synthetic ecosystem. In other words, the benchmark may still reward alignment with the authors’ own data generation style, taxonomy, and source distribution. This matters scientifically because the paper’s strongest claims are about general cybersecurity capability, not just competence on a benchmark derived from its own curation pipeline.

Related to that, the evidence that RedSage-Bench is a robust external benchmark is weaker than the paper suggests. Section 3.3, Pages 6 to 7, relies heavily on LLM generation, LLM verification, and LLM quality scoring, with human verification only clearly stated for the 240 open-ended pairs. For the 30K MCQs, the paper says random audits confirmed quality, but it does not report inter-annotator agreement, audit size, failure rate, or category-specific error patterns. Table 1 is used to argue benchmark completeness, but completeness is not the same as validity. A large synthetic benchmark can still be brittle, stylistically narrow, or biased toward the generator/verifier model family. This matters because several headline claims depend on RedSage-Bench being a trustworthy measurement instrument.

The open-ended evaluation is still too judge-dependent. On Page 7 and in Appendix C.2, the paper evaluates answer correctness and quality using an LLM-as-Judge rubric, with Llama-3.3-70B as the evaluator. The authors show qualitative judge outputs in Figure 15, which is useful, but that is not sufficient validation of the scoring pipeline. There is no systematic comparison against human raters, no judge agreement analysis, no variance estimate across judges, and no evidence that the judge does not favor the style of RedSage responses. This is especially important because the paper’s qualitative claim is not just that RedSage is more correct, but that DPO improves helpfulness and answer quality. Those are precisely the dimensions most vulnerable to judge bias.

The data curation and training setup has several under-specified parts that matter for reproducibility and interpretation. For example, the decontamination rule on Page 6 removes any synthetic post-training instance whose query has semantic similarity \(>0.9\) to a benchmark question, but the paper does not define the embedding model, whether similarity is cosine similarity \(s(q_i,q_j)=\frac{\langle e_i,e_j\rangle}{\|e_i\|\|e_j\|}\), whether embeddings are normalized, how the threshold 0.9 was chosen, or whether the matching is one-to-one or many-to-many. A threshold-based decontamination mechanism can change leakage conclusions a lot, so this should not be a hand-wave. Similarly, Section 3.4 says DPO uses the original Tulu-3 hyperparameters, but the main paper omits critical values such as the DPO temperature or \(\beta\), number of preference pairs, and the relative weight of DPO versus prior SFT data. These are not cosmetic omissions.

The continual pretraining story is slightly slippery in presentation. Section 3.1 on Page 4 first frames the corpus as 20 chronological chunks with early stopping after 5 chunks "to control training cost", while Appendix A.1 clarifies that the latest 5 chunks were selected as the final corpus. That is not the same thing as early stopping during a chronological pass; it is a corpus-selection decision favoring recent data. This may well be a good practical choice, but the current wording blurs the distinction. It matters because the paper informally interprets Figure 7 in the appendix as evidence of growing cybersecurity relevance over time, and then trains only on recent chunks. That combination may improve in-domain recency, but it also changes the benchmark fit story and should be presented more plainly.

The ablation coverage is decent but still not enough to support some of the stronger causal claims. Table 4 and Table 5 isolate CFW-only, Seed-only, Base, Ins, and DPO variants, but several important ingredients remain unablated: the 30% FineWeb-Edu replay ratio, the RedSage-Dump corpus, the agentic augmentation itself versus simpler non-agentic reformatting, the effect of SmolLM/SmolTalk integration, the exact contribution of DPO relative to SFT-only on external open-ended tasks, and the impact of the multi-stage verifier in benchmark creation. Figure 4 sells the planner/augmenter pipeline as a key innovation, but there is no experiment showing that this agentic augmentation outperforms a simpler template-based or direct prompting baseline with similar token budget. Without that, the paper risks attributing gains to the pipeline design when scale and source quality may be doing most of the work.

Some comparisons are not as clean as they first appear. In Table 4 on Page 8, RedSage-8B-Ins outperforms RedSage-8B-DPO on MCQs, while Figure 6 and the text on Page 7 suggest DPO improves open-ended quality. That is plausible, but the paper does not provide a principled discussion of this tradeoff or how users should choose between checkpoints. Likewise, Table 6 on Page 10 reports strong gains on general benchmarks after domain specialization plus SFT/DPO, but those models are also trained with substantial general instruction data and preference data. So the claim in the abstract that domain-aware pre/post-training improves general reasoning and instruction following is a bit too neat. The broader post-training recipe likely deserves some of that credit.

There is a methodological inconsistency in evaluation settings that makes some averages harder to interpret. On Page 7 and Page 9, base models are evaluated in text-completion mode and often with 5-shot prompting on external cybersecurity benchmarks, while instruction-tuned models are evaluated in 0-shot with chat templates. I understand why this is done, but then aggregated means across base and instruct groups should not be casually compared as if they reflect a single controlled axis. The paper is mostly careful about separating these blocks, but the prose occasionally slides into broader claims about "state of the art" without enough caveat about evaluation protocol differences.

The math and metric exposition is thinner than it should be for a paper making rigorous benchmark claims. The MCQ metric is described on Page 7 as normalized log-likelihood accuracy over options, but no explicit formula is given. If the score is computed as
\[
\hat{y}=\arg\max_{k\in\{A,B,C,D\}} \log p_\theta(k\mid x),
\]
that is fine, but "normalized log-likelihood accuracy" suggests some additional normalization that is not specified. For structured tasks like CTI-RCM, the paper also says it uses accuracy for consistency, which may be convenient, but this collapses richer task structure and may understate or overstate practical differences relative to the original benchmark metrics. The evaluation design is not invalid, but it is underspecified.

The qualitative examples are somewhat cherry-picked and would benefit from a more adversarial reading. Figures 12 to 14 highlight successes where RedSage is indeed better grounded. However, the paper does not pair these with failure cases, near-miss cases, or examples where domain-specific tuning hurts answer calibration. Figure 15 is also a double-edged sword: it demonstrates that the judge is strict about exact command syntax, which is good, but it also shows how a single alias or option-form mismatch can flip a response from detailed-and-useful to scored-as-false. Without validation that this strictness matches human judgments of operational correctness, the evaluation may be harsher or more brittle than intended.

The paper’s safety and release discussion is too short given the subject matter. Section 5 and the Ethics Statement on Page 11 acknowledge dual-use and mention research-only release and documentation, but that is pretty lightweight for a system explicitly trained on offensive skills, payload examples, CTF write-ups, and Kali tool usage. The paper does not describe any refusal behavior evaluation, misuse taxonomy, red-teaming results, or release gating strategy. This matters because the paper repeatedly emphasizes local deployability and privacy-preserving on-premise use, which is attractive for defenders but also lowers friction for misuse.

There is also a legal/compliance ambiguity in the data story. The Ethics Statement says some curated components may include copyrighted material and that such resources will not be redistributed without permission. That is a responsible statement, but it leaves unclear exactly what will be released, in what form, and whether replication of the published training recipe depends on assets that other researchers will not actually have access to. Since openness and reproducibility are part of the claimed contribution, this is not a minor administrative detail.

Finally, while the related work section covers direct cybersecurity LLM datasets and benchmarks reasonably well, the positioning is narrower than it should be around broader literature on LLMs in cybersecurity, especially safety, deployment risks, and evaluation paradigms. The paper would benefit from stronger contextualization relative to broader cybersecurity-LLM surveys and to interactive or resilience-oriented evaluation settings, rather than mostly comparing against prior corpora and static QA benchmarks. This does not invalidate the paper, but it weakens the framing.

## Questions
1. The decontamination step in Section 3.3 is potentially important, but currently too vague. What embedding model is used for semantic similarity, what exact similarity function is used, is it cosine similarity on normalized embeddings, and how was the threshold \(0.9\) calibrated? A small sensitivity study, for example thresholds \(0.8, 0.85, 0.9, 0.95\), would increase my confidence that the benchmark is not materially contaminated.

2. Can the authors provide a stronger validation of RedSage-Bench quality, especially for the 30K MCQs? Concretely, how many items were manually audited, by whom, on which categories, and what was the observed error rate? If possible, please report agreement between expert reviewers or at least a category-wise manual spot-check.

3. For the open-ended QA evaluation, how well do LLM-as-Judge scores align with human judgments? Even a modest study on the 240 open-ended items, using a subset scored by human annotators, would materially strengthen the conclusions around DPO improving answer quality.

4. Figure 4 argues for the planner-plus-augmenter design, but the empirical case for this specific agentic augmentation strategy is still indirect. Can the authors compare it against one or two simpler baselines, such as direct single-shot instruction generation from seed chunks or template-based QA/dialogue conversion at matched token budget?

5. Section 3.4 says DPO uses original hyperparameters, but the main paper does not provide enough details to interpret the tradeoffs between RedSage-8B-Ins and RedSage-8B-DPO. Please clarify the DPO setup, including \(\beta\), number of preference pairs, and why DPO improves open-ended quality while slightly reducing MCQ accuracy in Table 4.

6. The training description around the chronological chunks is confusing. Did the authors train sequentially through chunks 1 to 5 and stop, or did they intentionally select the latest five chunks as the final corpus before training? Please reconcile Section 3.1 with Appendix A.1.

7. What exactly will be released for the curated datasets, especially components derived from copyrighted or licensing-constrained sources? If some sources cannot be redistributed, can the authors specify whether they will release URLs, scripts, metadata, or filtered derived text only?

8. Given the offensive-security content, have the authors evaluated any safety properties of RedSage, for example refusal rates on clearly malicious requests, differential behavior across defensive vs offensive prompts, or compatibility with external policy layers? A brief additional analysis here would help.

## Flag For Ethics Review
- Yes, Legal compliance (e.g., GDPR, copyright, terms of use)  
- Yes, Potentially harmful insights, methodologies and applications  

## Details Of Ethics Concerns
The paper explicitly trains on offensive-security content, including hacking techniques, payload examples, CTF write-ups, penetration-testing workflows, and Kali tool usage, see Section 3.1 on Pages 4 to 5 and Table 3 on Page 5. This creates clear dual-use risk: the same model capabilities useful for defenders can also facilitate misuse, especially because the paper emphasizes local deployability and open release.

There is also a legal/compliance concern around copyrighted resources. The Ethics Statement on Page 11 acknowledges that some curated components may include publicly available but copyrighted resources and says those resources will not be redistributed without permission. That is responsible, but it leaves unresolved what exact artifacts will be released and whether the claimed openness/reproducibility depends on non-redistributable materials.

## Soundness Rating
3: good. The empirical work is broad and generally well executed, but some central claims depend on benchmark validity, decontamination details, and LLM-as-Judge evaluation choices that are not fully validated in the main paper.

## Presentation Rating
3: good. The paper is readable, well organized, and generally clear, with helpful figures and tables; however, several methodological details that matter for interpretation are under-specified or blurred.

## Contribution Rating
4: excellent. The combination of open cybersecurity corpus construction, agentic post-training data generation, a broad benchmark including tool proficiency, and strong empirical results makes this a meaningful contribution for the community.

## Overall Rating
6: Marginally above the acceptance threshold. But would not mind if paper is rejected. The paper makes a strong practical contribution and is likely valuable to the community, but the benchmark validation, judge-based evaluation, and several under-specified methodological choices prevent me from being more enthusiastic.

## Reviewer Confidence
4: confident. I am confident in the assessment and familiar with LLM training/evaluation and benchmark design, though some confidence-limiting factors remain because several critical implementation details are omitted from the main paper.