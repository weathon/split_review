# More effort is needed to protect pedestrian privacy in the era of AI

- Decision: Accept (Oral)
- Scores: 7, 8, 6

## Abstract
In the era of artificial intelligence (AI), pedestrian privacy is increasingly at risk. In research areas such as autonomous driving, computer vision, and surveillance, large datasets are often collected in public spaces, capturing pedestrians without consent or anonymization. These datasets are used to train systems that can identify, track, and analyze individuals, often without their knowledge. Although various technical methods and regional regulations have been proposed to address this issue, existing solutions are either insufficient to protect privacy or compromise data utility, thereby limiting their effectiveness for research. In this paper, we argue that more effort is needed to protect pedestrian privacy in the era of AI while maintaining data utility. We call on the AI and computer vision communities to take pedestrian privacy seriously and to rethink how pedestrian data are collected and anonymized. Collaboration with experts in law and ethics will also be essential for the responsible development of AI. Without stronger action, it will become increasingly difficult for individuals to protect their privacy, and public trust in AI may decline.

## Human Reviews

## Human Reviewer 1

### Rating
7

### Rating Number
7

### Confidence
3

### Summary
The paper makes a position on the need to protect pedestrian privacy that arises from the increasing colleciton and usage of datasets in public spaces. The authors briefly reviewed existing anonymization methods and proposed their viewpoint of a good privacy protection method. They listed a few misconceptions on pedestrian and anonymization methods and presented the challenges in this domain. Directions of future work is presented to call for collective efforts to deal with this issue.

### Strengths
The position is clear and the discussed issue on human privacy is important and timely. The arguments are relevant and clearly articulated.

### Weaknesses
Discussion of a good pedestrian privacy protection method is skechy. A more comprehensive discussion that covers more aspects with justificaitons are needed. Also "goodness" criteria may also be different depending on the applicaiton domain.

### Questions
What are other "goodness" metrics are relevant? Any guidelines on how to set "goodness" metric for different domains?
How to mitigage the inconsistencies of ethics policies in different regions/countries?

### Presentation
4

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This article deals with the increasing problem of data privacy, focusing on systems collecting pedestrian information. While the authors raised the problem, they discuss the trade-off of building meaningful and useful data-sets while keeping the pedestrian privacy

### Strengths
The topic is relevant to the community. The trade-off between privacy and usability is particularly interesting in the context of pedestrian privacy, and the reasoning is mainly well-presented. 

Authors discuss in a serious fashion the current methods for privacy protection, highlighting their limitations and arguing why they do not fully accomplish either the usability or the full protection of privacy.

### Weaknesses
The main weaknesses that I see are that what utility means is not clearly discussed. The limits of the concept "utility", or what the community will define as the utility of a data set, should be presented in a stronger way in the article.

### Questions
- What are the reasonable limits for "utility" of a dataset in your context? 
- What are the connections between the utility and privacy, and what should be acceptable for a democratic society?

### Presentation
4

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The paper is a position piece arguing that current ML practice does not adequately protect pedestrian privacy. It documents that widely used datasets for detection, tracking, intention prediction, and segmentation include clearly identifiable pedestrians collected without consent or meaningful anonymization. It surveys common protections, including cropping/blur/masks, full-body replacement, GAN-based anonymization, and explains why they fall short. Face-only methods leak identity via body, clothing, or gait.  Video methods often break temporal consistency; stronger methods are slow and can hurt downstream utility; generative replacements pose re-identification, bias, and copyright risks; federated learning is not a privacy guarantee; attacks on anonymizers are underexplored. 

The paper calls for privacy-by-design datasets and benchmarks, moves from face to full-body and gait anonymization, metrics and audits that test identity leakage, support for non-RGB modalities (thermal/event/LiDAR), fairness considerations, licensing/consent clarity, and collaboration with legal and policy experts.

### Strengths
It states a clear thesis that current practice fails to protect pedestrian privacy—and keeps the line tight throughout.  The paper shows widely used datasets where people are plainly identifiable and notes missing ethics safeguards, then ties this to risks of open access.  It explains why face-only methods are inadequate and points to identity leakage via body/clothing/gait and the pace of recognition advances. It surveys methods and uses prior results to argue that utility-preserving anonymization is achievable.  This counters the usual “privacy kills performance” claim. The piece is constructive and clearly identifies gaps (benchmarks, multimodal coverage, real-time) and calls for metrics and policy updates that the community can act on.

### Weaknesses
Could be improved by making the stance operational with a precise threat model and a measurable failure criterion, e.g., define identity leakage via $\max_{A\in\mathcal{A}}\Pr[A(T_\lambda(X),U)=Y]>\tau$. Then audit representative datasets, pre/post-anonymization re-ID and membership inference; utility–privacy Pareto for detection/tracking/intention; cross-modal linkage (RGB to/from thermal/event). Provide a reference pipeline, a numeric privacy score, and a license/consent checklist. Quantify non-RGB risks instead of asserting them. Report group-wise leakage/utility gaps and give mitigation if gaps exceed bounds. Clarify deployability with compute/latency budgets (e.g., 1080p\@30 fps on edge). Alternative positions: (i) controlled-access/DUA instead of heavy anonymization; (ii) governance-first accountability frameworks; (iii) redesign tasks to avoid identity exposure (skeleton/seg-only data).

### Questions
* Can you propose a **v0.1 Privacy Audit Starter Kit** (threat model, default attacker $A$, auxiliary data $U$, success bound $\tau$, baseline re-ID/MI tests, reporting template, code timeline)?
* Which **two or three tasks** should be privacy-formulated first (e.g., detection, tracking, intention prediction), and what objective/constraint form do you recommend?
* What minimum metrics and thresholds define success for v0.1 (e.g., re-ID AUC ≤ X at task mAP drop ≤ Y)?
* Which non-RGB modality should be addressed first, and what linkage baselines must any paper beat?
* What fairness audits are mandatory (groups, metrics, acceptable gaps), and what mitigation if gaps exceed bounds?
* What deployability budgets (hardware class, fps, latency, memory) should authors target for edge scenarios?
* Provide a simple decision rule for when to require controlled access/DUA vs heavier anonymization.

### Presentation
2
