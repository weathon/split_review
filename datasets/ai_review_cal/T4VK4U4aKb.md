- Decision: Reject
- Avg Score: 4.50
- Scores: 6, 6, 5, 1
Now I have thoroughly verified each claim against the paper. Let me produce the final consolidated review.

---

## Summary

This paper introduces a large-scale short-video platform dataset containing 10,000 users, 153,561 videos, and 1,019,568 interaction records. Its distinguishing contributions are (1) rich user behavior data (six explicit feedback types plus continuous watching time), (2) comprehensive user-side attributes (demographics, geography, device price), (3) a three-level hierarchical video category system (37/281/382 categories at Levels I/II/III), and (4) the first public short-video dataset to release raw video files (3.2 TB) along with pre-extracted Resnet-256 visual features and bilingual ASR transcripts. The paper validates the data through t-SNE visualizations, distributional analyses, and benchmarks with eight recommendation algorithms.

## Strengths

- **First public short-video dataset to include raw video files and preprocessed content features.** The paper provides all 153,561 raw videos (3.2 TB, 3,998 hours), plus Resnet-256 visual features and bilingual ASR transcripts (Section 2.3). No comparable public dataset (KuaiRec, REASONER, MicroLens) has released raw video content, which enables content-level analyses previously impossible with these datasets.

- **Larger and more diverse interaction data than comparable short-video datasets.** The dataset contains 1,019,568 interactions from 10,000 users over 153,561 videos, with six explicit feedback modalities (like, follow, forward, collect, comment, hate) and continuous watching time as implicit feedback. This substantially exceeds KuaiRec (1,411 users, 3,327 videos) and REASONER (2,997 users, 4,672 videos) on both user and video counts (Section 1, Figure 1).

- **Rich hierarchical category system with much finer granularity than prior work.** Videos are annotated with three levels (37 primary, 281 secondary, 382 tertiary categories), described in Section 2.2. This is far more detailed than the single-level categories in MicroVideo-1.7M and enables both coarse-grained analysis and fine-grained retrieval.

- **Comprehensive user-side attributes for social-science research.** The dataset includes demographic (age, gender), geographical (city, city level, community type), and device-price attributes (Section 2.2, Figure 5). These attributes are absent or scarce in Tenrec, MicroLens, and other benchmarks, enabling studies of fairness, regional bias, and addiction that require user-level covariates.

- **Quantitative benchmarking demonstrating practical usability.** Results for eight recommendation algorithms from BPR to multimodal methods (BM3, LGMRec) are reported in Table 1 (Section 3.1). The top performance of BM3, consistent with observations on other multimodal benchmarks, confirms the dataset functions as expected for standard recommendation evaluation.

## Weaknesses

### Fatal
None.

### Major

- **No discussion of copyright or redistribution rights for the raw video files.** The paper's headline contribution is releasing raw video files (Section 2.3), yet it never addresses whether the dataset has legal rights to redistribute 153,561 videos from 81,870 creators. The paper discusses consent from the 10,000 volunteer *users* whose behavior is tracked (Section 2.1) but says nothing about consent or licensing from the *video authors* who own the content. The paper states "the data collection procedure strictly follows privacy and ethical regulations" (Introduction, Section 2) but provides no specifics on how redistribution rights were obtained, whether a license (e.g., CC, research-only) governs the dataset, or what legal basis exists for re-hosting third-party copyrighted content. For a dataset release paper whose central innovation is raw video availability, this is a substantial documentation gap that could render the core contribution practically unusable. The authors must transparently address this before the dataset can be responsibly adopted by the community.

- **No statement on whether the platform authorized the data collection.** The paper reports collecting data from "10,000 volunteers on one of the largest short-video platforms" under their consent (Section 2.1), but does not state whether the platform itself authorized this collection or whether it complied with the platform's terms of service. Many platforms prohibit bulk data extraction or redistribution in their terms. Whether the collection was conducted with or without platform authorization is material information for a dataset paper.

### Minor

- **Central claim about video feature value is stated but not evidenced.** Section 3.4 states "there's a common performance drop without video features of all methods, demonstrating the value of extracted video features," but Table 1 only shows results *with* video features. No ablation table or comparison is presented in the paper. If this experiment exists in the supplementary material (which may have been stripped from the review copy), it should be clearly referenced; as presented, the claim is unsupported.

- **Imprecise scale claim.** The paper says the dataset "is larger than existing released datasets, e.g., Kuairec and REASONER" (Section 1, Line 22). This is true for those specific datasets but MicroVideo-1.7M (also cited) contains 1.7M videos. The claim should be scoped more precisely (e.g., "larger in user count and interaction diversity than existing released datasets") rather than stated as a blanket comparison.

- **No structured comparison table with existing datasets.** The paper qualitatively describes advantages over prior datasets in Sections 1 and 2.2 but does not provide a comparison table (rows = datasets, columns = behavior types, attribute fields, video content, scale). Such a table would let readers immediately assess the claimed advantages and is standard practice for dataset papers.

- **t-SNE visualization is a weak sole validation of content feature quality.** Figure 6 shows that visual embeddings separate by coarse category, which is a reasonable sanity check. However, this only demonstrates that features encode category-level information, not that they are informative for finer-grained tasks. Combined with the missing ablation (above), the validation of video content quality is thinner than it should be. Additional quantitative validation (e.g., retrieval precision, classification accuracy using the features) would strengthen this section.

### Trivial
- The abstract and introduction each refer to "video flies" (a typo for "files").
- The paper would benefit from stating the intended license (e.g., CC BY-NC 4.0) explicitly rather than providing only an anonymous download link.

## Nice-to-Haves
- An explicit IRB or ethics board approval statement would strengthen the ethical documentation.
- A brief ablation experiment in the main paper comparing recommendation results with and without video features would substantiate the claim in Section 3.4.
- Clarify what portion of the collected data is released (the first week only, or all six months).
- Concrete example pilot analyses (e.g., filter bubble extent computed using the hierarchical categories) would make the research directions in Section 4 more compelling.

## Removed Points

These points were flagged by reviewers but are not included as weaknesses for the reasons noted:

- **Minor-user data contradiction** — Removed because it is not a contradiction. The paper explicitly states (Line 69): "In the data analysis of the paper, we do not exclude the minor users but their data has been removed in the actual dataset." The analysis figures include minors for completeness; the released dataset excludes them. The paper is clear and consistent on this point.
- **Data period ambiguity** — Removed. The paper says "we collected six-month historical user interactions... while in the paper we focus on analyzing the first week's data for a quick release." This is a standard practice (full collection, sample release). Any ambiguity can be resolved with a one-sentence clarification.
- **Phone price privacy concern** — Removed because the paper explicitly states this was done "with the permission of volunteers" (Line 73). The concern is adequately addressed.
- **Generic Section 4 criticism** — Removed. Dataset papers commonly enumerate research directions without running experiments in each. This is not a flaw.
- **IRB-specific criticism** — Weakened to minor/trivial. The paper describes concrete privacy measures (user consent, ID hashing, minor data removal) even if it doesn't use the term "IRB." This is adequate for many venues.
- **"Cannot be independently verified" reproduction concern** — Removed per instructions. The paper provides an anonymous download link.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a perspective on the dataset or its implications that the paper itself does not already articulate. The most notable observation from the review process is that while the dataset fills a genuine gap in available resources, the paper's persuasiveness as a *data release* artifact is hampered by insufficient provenance documentation — a meta-level gap that is separable from the technical quality of the dataset itself.

## Suggestions

1. **Add a transparent Data Provenance and Ethics section** that explicitly addresses: (a) whether the platform authorized collection, (b) how redistribution rights for raw videos were obtained (or why they are not needed), (c) the license under which the dataset is released, and (d) IRB or equivalent ethics review. This is the single highest-leverage improvement for this paper.

2. **Include the ablation table** comparing recommendation performance with and without video features in the main paper (or clearly reference it if it exists in supplementary material).

3. **Add a structured comparison table** (dataset × attribute grid) to let readers immediately assess coverage against KuaiRec, REASONER, MicroVideo-1.7M, Tenrec, and MicroLens.

4. **Refine the scale claim** to be precise about which dimensions are larger (e.g., users, interaction types, attribute diversity) rather than claiming superiority on all axes.

5. **Strengthen content validation** with a quantitative metric (e.g., k-NN retrieval precision by category, or classification accuracy using extracted features) to complement the t-SNE visualization.
