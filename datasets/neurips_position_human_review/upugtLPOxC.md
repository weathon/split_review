# Don’t call it privacy-preserving or human-centric pose estimation if you don’t measure privacy

- Decision: Accept
- Scores: 7, 9, 4

## Abstract
This position paper argues that human pose estimation (HPE) cannot be considered privacy-preserving or human-centric unless privacy is measured and evaluated. Although privacy concerns have become more visible in recent years, HPE systems are still assessed almost exclusively using accuracy metrics. Privacy is neither defined in measurable terms nor linked to regulatory requirements, and common deployment architectures introduce additional risks due to data transmission and storage. We highlight the limitations of current practices, including the continued reliance on RGB inputs and the lack of benchmarks that reflect legal and ethical constraints. We call for a shift in evaluation practices: privacy must become part of how HPE systems are designed, tested, and compared.

## Human Reviews

## Human Reviewer 1

### Rating
7

### Rating Number
7

### Confidence
3

### Summary
Paper position: human pose estimation (HPE) must shift evaluation from performance-only to one that also includes measuring and prioritising privacy.

The paper argues that real world applications are deployed to environments where privacy, regulation, and practical constraints are mandatory. Yet, many high-accuracy HPE systems come with serious privacy risks. Although privacy has received more attention in recent HPE systems, privacy is evaluated without using metrics or referring to regulatory standards. The proposal here is that the community should work towards defining privacy as a measurable aspect of HPE, making it part of the system evaluation, to mitigate the gap between current research practices and the needs of privacy-aware real-world applications.

The paper outlines ways to preserve privacy, and factors that we can use to measure privacy. Finally, a number of alternative views are identified and argued against, supporting the paper position.

### Strengths
The paper gives a thorough assessment of ways to preserve and measure privacy, from practical and regulatory points of view. It discusses the performance vs privacy tradeoff, and argues for including both performance and privacy metrics in evaluation, making tradeoffs clear and comparable. These points clearly support the paper position. References can be found in almost every single argument. Alternative views are update-to-date and practical, and are addressed with reasonable arguments.

### Weaknesses
I do not see any major weakness in the paper. It has a strong, practical, and valid view point.

### Questions
I do not have any major question. To me, what has been asked here in the paper is just explicit clarity in privacy preserving when it comes to designing, training and evaluating HPE systems. But such extra data can bring about substantial benefits: in comparing and understanding HPE systems under different privacy preserving requirements, and in deploying such systems to regulated places.

### Presentation
3

---

## Human Reviewer 2

### Rating
9

### Rating Number
9

### Confidence
4

### Summary
This paper argues that human pose estimation (HPE) cannot be considered privacy-preserving or human-centric unless privacy is measured and evaluated. It outlines that frameworks are needed to help developers balance accuracy with privacy concerns.

### Strengths
This paper very clearly outlines the challenge with balancing privacy with accuracy in HPE, the existing privacy risk mitigation and why those techniques need to scored/evaluated and not just universally applied. I really enjoyed graphic 2. The paper engages with existing literature and contributes to a really important NeurIPS topic (HPE but also biometrics and medical AI).

### Weaknesses
The only section I struggled with was Section 3. The paper just starts referencing GDPR, the AI Act, and the PIPL. There is no explanation of what these laws are, where they are from (EU/China) and more importantly why choose these to inform the risks? The US still (for now) is a leader in AI/medical research so why not include HIPAA or Illinois Biometrics Law? Or why not look for a document from OECD/UN that outlines shared global principles? Just a bit more about these laws and why the authors chose them to frame the risks around them would be helpful.

### Questions
see above, I would love some insights into why the authors chose GDPR/PIPL to inform risks as opposed to other frameworks.

### Presentation
4

---

## Human Reviewer 3

### Rating
4

### Rating Number
4

### Confidence
4

### Summary
This paper holds the position that pose estimation must be more privacy focused and not potentially leak subject information. Towards that end, the paper proposes a few alternatives for human pose estimation that are more privacy preserving. Some of those alternatives are changing the input modalities in which the pose is estimated or change the representation for the human pose to be more privacy preserving. The paper also proposes a framework for determining privacy violations and the possible ramifications of violating it.

### Strengths
1. The paper is well written and quite comprehensive from a privacy analysis perspective 

2. Some of the risks are quite intuitive to understand

### Weaknesses
1. A major weakness of this paper in my opinion is the bundling of privacy breaches at the data input level (which are absolutely not specific to human pose estimation only) along with privacy breaches at the output which are potentially actually leaky

2. I don’t see very strong evidence that the predictions of human pose are actually leaking private information.

### Questions
1. How would we prove that private information of subject are actually being leaked by the pose estimation method? There’s a possibility, but unless I missed it (please do correct me!), it hasn’t been proven in the paper.

### Presentation
3
