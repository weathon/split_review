# OpenReview Should be Protected and Leveraged as a Community Asset for Research in the Era of LLMs

- Decision: Reject
- Scores: 5, 5, 5

## Abstract
In the era of large language models (LLMs), high-quality, domain-rich, and continuously evolving datasets capturing expert-level knowledge, core human values, and reasoning are increasingly valuable. **This position paper argues that OpenReview --- the continually evolving repository of peer reviews, author rebuttals, meta-reviews, and decision outcomes --- should be leveraged more broadly as a core _community asset_ for advancing research in the era of LLMs.** We highlight three promising areas in which OpenReview can uniquely contribute: enhancing the quality, scalability, and accountability of peer review processes; enabling meaningful, open-ended benchmarks rooted in genuine expert deliberation; and supporting alignment research through real-world interactions reflecting expert assessment, intentions, and scientific values. To better realize these opportunities, we suggest the community collaboratively explore standardized benchmarks and usage guidelines around OpenReview, inviting broader dialogue on responsible data use, ethical considerations, and collective stewardship.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper argues that the ML, AI community should make more use of OpenReview assets (reviews, discussions, ideations) to research LLM (and agents). The assets can be used for (1) peer reviewing, where LLMs are trained to produce better reviews and as such assist human reviewers (2) writing better research papers assisting authors to investigate new research topics, (3) aligning LLMs for better reasoning. As OpenReview contains multi-turn conversations and interactions between authors and reviewers, the authors believe that OpenReview asset will have the potential to enhance researches in related fields of LLMs (Agentic tasks, Open-Ended research).

### Strengths
-	Clear formatting, easy to follow, supported with evidences for each arguments.
-	Have addressed future work opportunities for each of the points raised.
-	Personally, the reviewer disagrees with the current position (which means that this paper will spark discussions and is worth being highlighted as a position paper). Fine-tuning LLMs for tasks relevant to OpenReview can potentially encourage the misuse of LLMs by reviewers in current review practices. As such, rather than promoting OpenReview for benchmarks, OpenReview should ban the utilization of discussion data for benchmarks. Would be happy to hear the author’s thought on this.

### Weaknesses
-	While OpenReview contains a large number of discussions, the data is mostly limited to ICLR conferences. Other conferences only have 1-2 years of history of releasing author-review discussions. As such, the constructed task and dataset might be extremely narrow. Have the authors taken this into consideration? How does the datasets listed in Table 1 and the proposed dataset devoid from this problem?
-	The reviewer is also concerned that creating and promoting such tasks from the OpenReview will only accelerate the current misuse of LLMs for reviewing (using LLMs to generate reviews). It would be nice to enforce these discussions in 7.Alternative Views first section.
-	It might be helpful to consider and discuss the below papers which seems quite relevant to this work.

[1] Mapping the increasing use of llms in scientific papers 

[2] Position: The AI conference peer review crisis demands author feedback and reviewer rewards

### Questions
-	The current status quo of OpenReview assets has not been thoroughly discussed in this paper. While Table 1 provides a list of tasks related to OpenReview, it is simply a list of works. A more thorough analysis of the current tasks and how the new tasks should be set should be more specific in details.
-	Why can't existing datasets be used for the arguments made in the paper? What is the major bottleneck to utilizing these assets as a training dataset for LLMs?
-	The reviewer has personally collected ICLR review datasets for experiments. One of the major problems was the inconsistency in peer review questions and criteria every year. As such, the structure is not unified throughout the years. How can we handle such practical problems?
-	The reviewer is slightly confused about why this paper was submitted as a position paper, but not to a dataset & benchmark track. What is stopping the authors from creating such a dataset?

### Presentation
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This position paper argues that OpenReview as a continually evolving repository of peer reviews, author rebuttals, meta-reviews, and decision outcomes should be leveraged as a core community asset for advancing LLM research. The authors highlight three key application areas: (1) enhancing peer review quality, scalability, and accountability through automated assistance and protection tools; (2) enabling open-ended benchmarks rooted in genuine expert deliberation to support model evaluation and post-training; and (3) providing high quality datasets for alignment research that capture real-world expert interactions, intentions, and scientific values. They propose collaborative exploration of standardized benchmarks, ethical guidelines, and usage protocols to ensure responsible and beneficial use of OpenReview data. The central position is that, with proper safeguards and stewardship, OpenReview can uniquely advance LLM capabilities while strengthening the research community.

### Strengths
The paper’s strongest contribution is its articulation of three concrete use cases for leveraging OpenReview in LLM workflows: assisting and protecting peer review, enabling open-ended task evaluation and post-training, and creating a high quality dataset for alignment and reasoning. The peer review assistance case is well developed, listing specific automated tasks such as review drafting, rebuttal mediation, calibration checks, and meta-review generation, with opportunities that are actionable and relevant to current conference workflows. The open-ended task evaluation section clearly positions OpenReview as a rich, corpus driven by experts and identifies distinct supervision streams, while the alignment and reasoning case compellingly frames multi-round peer review as a realistic setting for deliberative reasoning and pluralistic value alignment. These use cases show a practical vision for bridging peer review infrastructure and LLM development using OpenReview.

### Weaknesses
The three proposed use cases are unevenly developed. Peer-review assistance is described with specific example tasks, but lacks concrete deployment plans, governance structures, or evidence of effectiveness. The open-ended evaluation and alignment applications are presented largely at a conceptual level, with minimal detail on benchmarking protocols, success metrics, or mechanisms to address bias, data leakage, and disagreement modeling. Across all cases, the paper provides limited discussion of privacy protections, consent processes, and ethical safeguards, which are critical when handling sensitive review data. No pilot studies, simulations, or feasibility analyses are offered to assess practicality, cost, or integration with existing OpenReview workflows. Without clearer implementation pathways and risk mitigation strategies, the proposals remain speculative, leaving uncertainty about how they would be operationalized or adopted by the community.

### Questions
How do you envision addressing privacy, consent, and governance concerns when using sensitive review data for LLM training and evaluation, particularly in light of potential reviewer identification risks?
How would you mitigate the risk of bias or overfitting in LLMs trained on OpenReview data, given the narrow domain and potential systemic patterns in reviewer judgments?

### Presentation
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper argues that OpenReview should be treated as a shared, protected community asset for research in the LLM era. It outlines how OpenReview data could enhance peer review quality and scalability, provide expert-grounded benchmarks for open-ended LLM tasks, and serve as a rich source for alignment and reasoning research. It also addresses structural risks to review quality from rapid conference growth and calls for standardized benchmarks and responsible stewardship.

### Strengths
- Clearly identifies multiple concrete use cases (peer review enhancement, open-ended LLM evaluation, alignment research) with detailed examples of possible applications.
- Highlights the unique value of OpenReview data (expert-authored, multi-round, domain-specific) compared to synthetic or crowd-sourced datasets.
- Incorporates discussion of ethical considerations, alternative perspectives, and risks of over-automation in peer review.

### Weaknesses
- The proposed actions (e.g., benchmark creation, stewardship mechanisms) remain high-level without concrete implementation roadmaps or prioritization.
- Limited empirical evidence or case studies demonstrating feasibility of the proposed LLM-assisted peer review improvements.
- Risks of bias and inconsistency in peer review data are acknowledged but not deeply addressed in terms of mitigation strategies beyond general “quality protection.”
- The openreview data could be biased, subjective, and even noisy, which should be addressed.

### Questions
na

### Presentation
3
