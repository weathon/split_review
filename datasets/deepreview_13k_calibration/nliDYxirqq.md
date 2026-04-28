# EduGym: An Environment Suite for Reinforcement Learning Education

- Decision: Reject
- Avg Score: 4.20
- Scores: 3, 3, 6, 3, 6

## Abstract
Due to the empirical success of reinforcement learning, an increasing number of students study the subject. However, from our practical teaching experience, we see students entering the field (bachelor, master and early PhD) often struggle. On the one hand, textbooks and (online) lectures provide the fundamentals, but students find it hard to translate between equations and code. On the other hand, public codebases do provide practical examples, but the implemented algorithms tend to be complex, and the underlying test environments contain multiple reinforcement learning challenges at once. Although this is realistic from a research perspective, it often hinders educational conceptual understanding. To solve this issue we introduce EduGym, as a set of educational reinforcement learning environments and associated interactive notebooks tailored for education. Each EduGym environment is specifically designed to illustrate a certain aspect/challenge of reinforcement learning (e.g., exploration, partial observability, stochasticity, etc.), while the associated interactive notebook explains the challenge and its possible solution approaches, connecting equations and code in a single document. An evaluation among RL students and researchers shows 86% of them think EduGym is a useful tool for reinforcement learning education. All notebooks are available from https://sites.google.com/view/edu-gym/home, while the full software package can be installed from www.github.com/anonymized.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces a software environment for learning reinforcement learning. The software consists of a number of environments, explanations, and accompanying notebooks. The authors also conducted a human evaluation study and found that the majority of the participants find the proposed tool helpful.

### Strengths
This new RL environment for learning sounds like an exciting addition to the existing learning materials to help beginners to get into this field. The selection of problems and the sequence of presenting them seem well considered. The notebooks are detailed and easy to read. I think this will be a good educational resource.

### Weaknesses
The main contribution of this paper seems to be the creation of a new tool, software package, environment, and notebooks for learning RL. I am not sure how such contribution suits the themes at ICLR. While such new learning materials are welcomed, it lacks scientific rigor I am expecting from an ICLR contribution. In particular, the authors claim that the proposed environment is simpler and easier for people to learn RL. While the design of the proposed environment is supported by several reference literature articles, there is no comparison studies to demonstrate that the proposed environment is simpler, easier to learn, and overall better than other existing RL learning materials.

In addition, although the evaluation results show that EduGym improves learning outcomes, this is measured by self-reported survey. There is no other evaluative methods to assess learning, nor any kind of comparison (or A/B testing) to existing tools to benchmark the effectiveness of EduGym, without which it is difficult to understand the educational utility of the proposed environment.

To summarize, 1) this paper in my opinion is a good educational contribution rather than a technical contribution, which seems to me a unsuitable contribution for ICLR; 2) the paper lacks scientific rigor in terms of evaluating the utility of EduGym.

### Questions
I don't have questions for the authors.

### Soundness
2 fair

### Presentation
3 good

### Contribution
1 poor

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper introduces EduGym, a suite of educational reinforcement learning environments and interactive notebooks designed to address the struggles faced by students in understanding and applying reinforcement learning concepts. EduGym provides specific environments that illustrate different challenges in reinforcement learning, such as exploration, partial observability, and stochasticity, allowing students to gain practical experience. It simplifies the learning process, provides insight, and offers a quick experimentation loop for students, catering to their educational needs.

### Strengths
- I can see the big effort of the authors to build EduGym and kind motivation to help students to learn reinforcement learning.
- Providing interactive notebooks that explain the challenges, possible solution approaches, and experimental performance of each environment.

### Weaknesses
However, my main concern is that this paper is not a research paper w.r.t. solving existing research problems or proposing new problems. This paper is more like a piece of description or instruction. This paper should be submitted to the dataset/benchmark track or blog post track, instead of the main track of ICLR.

### Questions
I went through the provided Jupyter Notebook and found the authors did a really good job for the RL beginner. However, I still suggest the authors submit this paper to other tracks.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces EduGym, an educational tool for reinforcement learning, designed to address the challenges students face in understanding and applying RL concepts. It provides a set of educational RL environments, each tailored to isolate specific RL challenges, along with interactive notebooks that bridge the gap between equations and practical code, aiding in faster learning progress.

### Strengths
- The paper addresses a real-world issue faced by students entering the field of reinforcement learning, making it highly relevant and practical for both educators and learners.
- EduGym introduces a novel solution by providing a set of educational RL environments and interactive notebooks, which can enhance the understanding of RL concepts through hands-on experimentation.
- EduGym provides comprehensive coverage over various aspects of RL.

### Weaknesses
 - The background section seems to be irrelevant as it hasn't been used, referred to, or elaborated in the rest of the paper.
- The lack of introduction to basic RL algorithms like value iteration or REINFORCE [1].
- Lack of innovation.

### Questions
- It would be beneficial to include information about the pedagogical principles or educational theories that guided the development of EduGym. How was the content structured to support effective learning, and were any instructional design models considered?
- While EduGym is presented as a solution to the challenges in RL education, are there any plans to expand its content, incorporate new challenges, or update the environments and notebooks in the future to keep pace with evolving RL research?
- What is the plan for maintaining and updating EduGym to keep it relevant and aligned with the latest developments in RL research and education?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper introduces a library named EduGym, which is a set of educational RL environments and interactive notebooks. It aims address the challenges students  encounter in studying RL. With EduGym, students can translate between equations and code in a cohesive manner by interactive notebooks that explain the challenges and their potential solutions. An evaluation conducted among RL students and researchers indicates that 86% of them find EduGym to be a valuable tool for reinforcement learning education.

### Strengths
**Originality:**

EduGym is an educational library for RL students. Its key novelty are: (1) it provides a set of educational RL environments each specifically designed for a particular RL challenge; (2) to better illustrates RL concepts, it a set of interactive notebooks, where students are gradually taught about each challenge, and can at the same time actively experiment with relevant code. 

**Quality:**

This paper developed many RL environments (e.g., exploration, partial observability, stochasticity, etc.) and provided high-quality code for students to learn RL.

**Clarity:**

This paper has a clear motivation and the whole paper is easy to follow.

**Significance:**

In the educational context, this paper has a positive impact on teaching RL.

### Weaknesses
Despite the merit of this paper, weaknesses of this paper are:

1. There is no key contribution to RL algorithm and research. This paper introduces an educational library for RL learners. Its key contribution is limited to RL teaching, which is not the key scope of ICLR conference.
2. There are many excellent libraries for RL researchers and learners, such as OpenAI’s Spinning Up library and the code of Sutton and Barto’s RL book. Spinning UP provides simple and highly-consistent code for (Deep) RL researchers and practitioners. The code of Sutton and Barto’s RL book also provides example for students to understand concepts, such as the Markov chain example in Q-learning and Double Q-learning. Environments in EduGym are deliberately designed but are not conceptually novel in RL research. EduGym does not provide any guidance for RL practitioners.
3. It lacks best practices on how to use deep neural networks in RL.

### Questions
What sets EduGym apart from Sutton and Barto’s RL book and its code?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a novel suite, EduGym, for guiding students to learn about RL. EduGym proposes several simple environments that demonstrate the unique challenges in RL. It also provides notebooks for a quick start on these environments. The authors interviewed junior graduate students about EduGym, and most students think that it help them improve understanding in RL.

### Strengths
Learning RL is always a hard task for junior graduate students, as it requires a lot of basic knowledge (MDPs, dynamics programming, etc.), as well as broad knowledge about current progress and challenges in DRL.  Although there have been textbooks like RL: An Introduction, it mainly focuses on traditional RL, and has few discussions about DRL. Meanwhile, there have been some people who make RL lectures online, but they can hardly contain all the critical challenges in DRL. EduGym serves as a good first step towards a powerful toolkit that enables a direct demonstration to current DRL challenges.

### Weaknesses
The authors do not provide information about whether open-sourcing their codes. EduGym has the potential of becoming a powerful toolkit for starting RL research, if it can be jointly maintained by the RL community.

### Questions
1. Do the authors plan to open-source the codes, and invite the community to jointly maintain the codebase?
2. Do the authors plan to add more examples on more RL methods like target network, double Q networks, etc?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good
