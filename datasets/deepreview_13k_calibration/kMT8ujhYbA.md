# Catastrophic Cyber Capabilities Benchmark (3CB): Robustly Evaluating LLM Agent Cyber Offense Capabilities

- Decision: Reject
- Avg Score: 5.33
- Scores: 3, 8, 5

## Abstract
LLM agents have the potential to revolutionize defensive cyber operations, but their offensive capabilities are not yet fully understood. To prepare for emerging threats, model developers and governments are evaluating the cyber capabilities of foundation models. However, these assessments often lack transparency and a comprehensive focus on offensive capabilities. In response, we introduce the Catastrophic Cyber Capabilities Benchmark (3CB), a novel framework designed to rigorously assess the real-world offensive capabilities of LLM agents. Our evaluation of modern LLMs on 3CB reveals that frontier models, such as GPT-4o and Claude 3.5 Sonnet, can perform offensive tasks such as reconnaissance and exploitation across domains ranging from binary analysis to web technologies. Conversely, smaller open-source models exhibit limited offensive capabilities. Our software solution and the corresponding benchmark provides a critical tool to reduce the gap between rapidly improving capabilities and robustness of cyber offense evaluations, aiding in the safer deployment and regulation of these powerful technologies.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes a framework and benchmark of 15 challenges that allows a LLM to conduct attacks. They evaluate a number of LLMs in this framework.

### Strengths
This is a benchmarks paper and I believe the authors have chosen a primary area that is not suited for this paper. If I evaluate this according to the choice of authors' choice of primary area, then this paper should be rejected as there is no new technique in safety, alignment, privacy, or social considerations.

Merits:
1) The problem is interesting and a good direction to study and benchmark the behavior of LLMs.
2) The experiments have been done extensively (but as acknowledged by authors, not covering all tactics)
3) This can be a valuable basis for further engineering.

### Weaknesses
Weakness:
1) This line "While some benchmarks claim to measure general cyber capabilities but only cover specific sub-capabilities, 3CB ensures that each challenge is designed such that successful completion by a model accurately reflects its ability to apply the technique described in that challenge." First, this line requires citations to the "some" benchmarks and then I did not understand how 3CB ensures that each challenge is designed such that successful completion by a model accurately reflects its ability to apply the technique described in that challenge? Where is the evidence for this claim?
2) Also, the authors claim novelty of the challenges - how is this ensured. Particularly, when the challenges are broadly in the known ATT&CK category? Also, LLMs can easily relate similar (but not same) textual concepts, so where is the this novelty coming from - are these conceptually new challenges?
3) Related to above, the authors say 11 challenges are publicly released - does this mean on the internet?
4) There are many open questions arising from the work, some of which should be done to make the work stronger? Will a cybersecurity-specific finetuned smaller LLM (like Llamma) do better? Clearly, large LLM like GPT have many advantages in terms of training data and size of model, more fine-grained comparison of why these succeed and smaller LLM fail is needed.

### Questions
Please respond to the weaknesses.

### Soundness
3

### Presentation
3

### Contribution
1

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper proposes an evaluation framework of state of the art LLM agents in their capabilities to carry out offensive cybersecurity tasks. Based on the MITRE ATT&CK framework, they propose 15 cybersecurity challenges, representing the 15 attack categories (one from each category) of the ATT&CK framework, that they use to evaluate the capabilities of 14 LLM agents in completing successfully each challenge. Each challenge is attempted 10 times with the best elicitation variation. Then, a linear mixed-effects model is used to quantify each agent's performance. The experimental results show a variability in the rate of completion between LLM agents, the best being the larger ones (GPT-4 and Claude 3.5 Sonnet). They also reveal a variability due to the communication protocol used by the agent, notably, XML outperforming Markdown and XML. The overall conclusion of the paper is that the proposed 3CB framework shows that LLMs (mainly the large ones) are capable of sophisticated cyber operations and hence their use in cybersecurity offensive operations should be regulated.

### Strengths
On the positive side, 
1) The paper is very well written and enjoyable to read.
2) The topic is timely and very relevant, as penetration testing is still a manual process heavily involving human agents who need to be trained on offensive tactics and requiring a high technical expertise. Such framework is very welcome for organizations who opt for an offensive security strategy to harden their system security.
3) The proposed framework is a good step towards leveraging the capabilities of state of the art LLM agents for cybersecurity offensive tasks.
4) The approach is comprehensive as it covers all the categories of cybersecurity attacks (according to MITRE) and is evaluated on the major LLM agents currently.

### Weaknesses
On the negative side,
1) In my opinion, the paper does not show clearly the capabilities of LLM agents in cybersecurity offensive operations. Apart from the (good) example in Appendix B.2, as a reader I couldn't gauge the capabilities of the LLMs in cybersecurity attacks.
2) For example, the proposed challenges in Table 1 come with brief descriptions that does not allow to assess how simple/sophisticated they are. Take the first challenge, nmap, to me it is a straightforward challenge. Then, when you check the rate of completion for the various LLMs (Figure 4), you notice that not all LLMs could complete it. In particular, binpwn, which is a more demanding challenge, has a better completion rate. I find this very strange. Also if you take the setuid, you notice a higher completion rate than nmap. This suggests that setuid is even simpler than nmap ! I find these results counterintuitive and do not help to gauge well the capabilities of the LLMs.
3) Apart from binpwn, no details are provided for the other challenges (I understand that 4 of them are kept confidential on purpose). I tried to get those details from the github repository, but as far as I saw, it contains just a demo of again the binpwn. Nothing on the other challenges. I may be wrong. 
4) I couldn't run the code because the repository lacks clear instructions on how to install the software and run it.  

So as recommendation, I would suggest providing more details about each challenge (in an extensive version of Table 1, or better yet, in the appendix, similair to binpwn). Also, list all the prompts used in the evaluation (in the appendix or in the github).

### Questions
1) How the prompts are chosen for each challenge? As I understand, several prompts were used for every challenge.
2) Some challenges require specific environment setup (VMs, specific network configuration, etc.). How those environment requirements are handled in the framework ?
3) Can you explain why some LLMs complete some sophisticated challenges but fail in simpler ones ? This is crucial to understand better the capabilities of the LLMs in cybersecurity offensive operations.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces a new benchmark called 3CB, which includes 15 challenges used to evaluate the cyber offensive capabilities of different LLMs. This paper then conducts experiments on a set of agents with different LLMs and shows that larger LLMs tend to have stronger cyber offensive capabilities than smaller LLMs.

### Strengths
1. The motivation is reasonable and has real-world implications.

2. This is the first benchmark for evaluating the catastrophic cyber capabilities of LLMs.

### Weaknesses
Although the authors claim that this is the first comprehensive benchmark for evaluating the catastrophic cyber offensive capabilities of LLMs, the technical contribution is not strong enough to pass the high bar of ICLR. The presentation of the paper is more like a technical report, which is not as well-organized as a technical research paper. For experiments, only some superficial results are obtained, e.g., larger LLMs tend to have stronger cyber offensive capabilities than smaller LLMs, which makes the paper seem neither suitable for a technical paper nor a dataset/benchmark paper (in some other top conferences). Therefore, there is a quite large space for improvement before the paper is ready for acceptance.

### Questions
See Weaknesses.

### Soundness
2

### Presentation
2

### Contribution
2
