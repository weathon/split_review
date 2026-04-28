# Saliency-Guided Hidden Associative Replay for Continual Learning

- Decision: Reject
- Avg Score: 3.60
- Scores: 6, 3, 3, 3, 3

## Abstract
label{sec: abstract}
Continual Learning (CL) is a burgeoning domain in next-generation AI, focusing on training neural networks over a sequence of tasks akin to human learning. While CL provides an edge over traditional supervised learning, its central challenge remains to counteract \emph{catastrophic forgetting} and ensure the retention of prior tasks during subsequent learning. Amongst various strategies to tackle this, replay-based methods have emerged as preeminent, echoing biological memory mechanisms. However, these methods are memory-intensive, often preserving entire data samples—an approach inconsistent with humans' selective memory retention of salient experiences. While some recent works have explored the storage of only significant portions of data in episodic memory, the inherent nature of partial data necessitates innovative retrieval mechanisms. Current solutions, like inpainting, approximate full data reconstruction from partial cues, a method that diverges from genuine human memory processes. Addressing these nuances, this paper presents the \textbf{\underline{S}}aliency-Guided \textbf{\underline{H}}idden \textbf{\underline{A}}ssociative \textbf{\underline{R}}eplay for \textbf{\underline{C}}ontinual Learning (\textbf{SHARC}). This novel framework synergizes associative memory with replay-based strategies. SHARC primarily archives salient data segments via sparse memory encoding. Importantly, by harnessing associative memory paradigms, it introduces a content-focused memory retrieval mechanism, promising swift and near-perfect recall, bringing CL a step closer to authentic human memory processes. Extensive experimental results demonstrate the effectiveness of our proposed method for various continual learning tasks~\footnote{Preprint. Do not distribute.}.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper introduces the Saliency-Guided Hidden Associative Replay (SHARC) framework, which combines associative memory with replay-based strategies to address catastrophic forgetting in Continual Learning. Firstly, SHARC archives only the most salient segments of data through sparse memory encoding, making it memory-efficient. Secondly, this paper proposes a content-centric memory retrieval module inspired by associative memory, enabling swift and impeccable recall capabilities. Extensive experimental results demonstrate the efficacy and superiority of the proposed SHARC framework for various continual learning tasks .

### Strengths
The paper introduces the novel Saliency-Guided Hidden Associative Replay (SHARC) framework, which combines associative memory with replay-based strategies to address catastrophic forgetting in Continual Learning. 
The proposed SHARC framework demonstrates its effectiveness through extensive experimental results on various continual learning tasks, showcasing its superiority in mitigating forgetting and achieving better recall. 
The structure of SHARC is sparsity, which is hardware-friendly and can lead to memory cost reduction instantly.

### Weaknesses
The paper does not provide a comprehensive comparison with existing replay-based methods for Continual Learning, making it difficult to assess the superiority of the proposed framework. Specifically, the paper lacks a detailed analysis of how SHARC performs against state-of-the-art replay methods across various benchmark datasets and task sequences. This makes it challenging to ascertain whether the gains observed are due to the novel aspects of SHARC or simply a consequence of using a replay mechanism. Furthermore, the paper needs to clarify the specific replay strategies that SHARC is being compared against, including their memory buffer sizes and replay frequencies, to allow for a fair evaluation.

While the paper introduces a content-focused memory retrieval mechanism, it lacks detailed explanation and analysis of how this mechanism works and its impact on recall performance. The paper does not provide a clear mathematical formulation of the associative memory retrieval process, making it difficult to understand the underlying mechanism. It also fails to analyze the computational complexity of the retrieval process, which is crucial for evaluating its scalability and efficiency. Additionally, there is no ablation study to demonstrate the impact of different components of the retrieval mechanism on the overall performance.

### Questions
It would be beneficial to include a comprehensive comparison with existing replay-based methods for Continual Learning to highlight the advantages and limitations of the proposed framework.
Could the authors provide a more detailed explanation and analysis of the content-focused memory retrieval mechanism introduced in the SHARC framework? This would help in understanding how this mechanism works and its impact on recall performance.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
In conventional replay-based continual learning methods, raw/ entire data are stored and recalled during replay which is biologically implausible and memory intensive. This work presents a biologically plausible framework where partial salient data are stored and complete data are retrieved during replay. It utilizes sparse memory encoding to store partial information and a content-based memory retrieval mechanism to recover complete information. It enables efficient memory storage and archives better recall accuracy than generative models. This work has potential to perform effectively in highly memory-constrained applications.

### Strengths
This paper presents bio-inspired perspectives to store hidden sparse representations and associate memory based recall. This resembles how humans and animals learn by compressing information.

Innovative approach of storing and retrieving rehearsal data for memory efficient replay and mitigating catastrophic forgetting.

Saliency based approach to store sparse information which leads to increased memory efficiency.

Associate memory based retrieval offers fast and efficient recall and higher noise tolerance. This is an innovative approach to reduce memory footprint and computational overhead in continual learning.

Memory-forgetting mechanism to remove more data from old tasks than new tasks.

Several SOTA methods show improved performance when combined with proposed method, SHARC

### Weaknesses
Lack of experiments on high dimensional and large scale datasets e.g., ImageNet-1K. Many algorithms do not scale for large numbers of classes and high-dimensional inputs. It is 2023 and people have been using ImageNet for continual learning for at least 7 years. I'm assuming this is because they are starting with an ImageNet pre-trained backbone, but that is also a problem given the datasets studied. Mini-imageNet is not an appropriate test set using an ImageNet pre-trained backbone. MNIST and CIFAR are also extremely inappropriate. This is throwing a comparatively very powerful network at toy problems, where training its output layer alone likely yields extremely high results.

The model is only tested for an extreme edge case in continual learning (class incremental learning). Other distributions need to be studied, IID, etc. Given the neuroinspiration, this is especially important, but it conflates the goals of continual learning (knowledge accumulation over time) with the test (learning classes one at a time). An ideal continual learner should be robust to any data orderings including class incremental learning and IID.

Limited representation learning. It keeps the feature backbone frozen and trains the classifier head and associative memory network. Thus the model has limitations in learning representations in hidden layers which might be necessary for learning new tasks. It is unclear how model depth impacts retrieval performance, for example when we want to store and retrieve information in the earlier layers close to input.

Given ImageNet-1K pretrained backbone, selected datasets e.g., MNIST, CIFAR-10 / 100, and mini-ImageNet seem less challenging for a continual learner. It is also unclear how ImageNet-1K (224x224) pretrained network is used for small datasets consisting of lower resolution images (32x32).

Since SHARC requires training associate memory unlike comparison methods. Comparing methods based on the same bounded compute (same amount of training updates) will be fairer.

Sometimes SHARC under-performs some baselines (Table 2 and Table 4). It is unclear if SHARC provides consistent performance gain across CL settings / methods/ datasets/ buffer sizes. It is claimed that DER++ equipped with SHARC achieves a 45.5% improvement in accuracy on S-CIFAR-100 but results in Table 2 do not support this claim.

The experiments and evaluation leave a great deal to be desired. Using an ImageNet-1K pre-trained backbone is fine, but then the experiments would need to be appropriate, for example, learning a dataset like iNaturalist or Places-365, and then trying multiple different distributions, including incremental class learning. Also, more experimental comparisons against recent methods and benchmarking in a fair way where all models are compared with the same setup would be more sound. 

The method needs to demonstrate some sort of efficiency or other value in some sense.

The method is interesting, but the evaluation and experimental confounds mean the paper is not ready for publication. I encourage the authors to redesign their experiments, eliminate confounds, study multiple distributions, and to study much larger and more appropriate datasets. It requires relatively few resources to train an ImageNet-1K model and can be done with cloud computing for very little money.

### Questions
In Fig.1, spatial information was retrieved but in the main experiment channel information was recovered. If you mask out spatial information, can you apply similar associate memory to retrieve complete information?

What happens if you train more layers of DNN besides the final layer?

What is the computational overhead for training associate memory? Does associate memory increase inference cost?

How do you initialize the last layer before continual learning begins?

How do you use ImageNet-1K (224x224) pretrained network for small datasets consisting of lower resolution images (32x32)?

Besides Fig.1, do you have results to support the claims about fast and efficient recall and noise tolerance?

### Soundness
1 poor

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper introduces a novel framework called Saliency-Guided Hidden Associative Replay for Continual Learning (SHARC) to address the challenge of catastrophic forgetting in continual learning. 

In this paper, we provide a plugin to enhance the performance of replay-based continual learning methods to improve storage efficiency.

The paper proposes the SHARC framework, which combines associative memory with replay-based strategies. SHARC encodes and archives salient data segments using sparse memory encoding. By leveraging associative memory paradigms, SHARC introduces a content-focused memory retrieval mechanism, promising quick and accurate recall.

 The associative memory creates an additional memory footprint and consumes a lot of computing resources for updating it.

The paper presents extensive experimental results that demonstrate the effectiveness of SHARC for various continual learning tasks.

### Strengths
The proposed method can be seamlessly adapted to any replay-based approach, improving their performance in various continual learning scenarios. 

The experimental results provide evidence of the effectiveness of SHARC in improving the performance of replay-based methods.

### Weaknesses
Lack of detailed network and hyper-parameter configuration, especially, for associative memory networks.

The lack of recent baselines in the experiment, most of the baselines used were proposed two or three years ago.

The associative memory A(x,ω) is implemented as a recurrent or feed-forward neural network. The associative memory creates an additional memory footprint, and consumes a lot of computing resources for updating it.

The experiments in this paper do not seem to be reasonable. The method in this paper introduces an additional associative memory network to store more information for replay, which definitely makes the original method perform better.

### Questions
How much memory and computing resources does associative memory take up? Wouldn't it be better if those extra storage resources were used to store more exemplars? Please make a comparison.

### Soundness
2 fair

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
Paper proposes a novel Continual Learning (CL) method, SHARC, inspired by biological memory (selective memory retention of salient experience). It has 2 novel contributions to the CL problem: saliency selection of feature channels and Associative Memory (AM) to improve memory efficiency and mitigate forgetting. The empirical experiments for the Task-IL and the Class-IL settings show significant improvement over the SOTA replay CL methods like GEM, A-GEM, ER, etc.

### Strengths
Paper's position is that the biological inspired architecture for CL is more memory efficient and can outperform the current replay methods which either stores the entire representation or approximately generate the training data for older classes. This motivation is supported by the strong experimental results.

### Weaknesses
1. The novelty of the paper is limited as it combines existing methods such as "saliency" and "associative memory" for the CL problem. In image retrieval literature, there are several prior works which combine both mechanisms. See references below. As such, the real novelty lies only in the application of these 2 mechanism to the CL problem.

2. (Minor) Experiments only include replay-based CL methods. As mentioned in the paper's related works, replay methods are among the strongest in CL. However, this design leaves a big unknown about how well the proposed method compare against other approaches, like regularization-based and dynamic architecture-based. Only DER++ which has regularization and rehearsal is included.

3. (minor) The implementation details about how SHARC combine with the other baseline methods are not given. However, this is somewhat mitigated by the inclusion of anonymous codes. I did not inspect the codes, however.

REVISED: See major weakness from Reviewer WbsA.

### Questions
1. (Section 5.2) How does the proposed method combine with the 6 replay-based methods? Does the SHARC Memory Replay module directly replace the respective methods' original replay mechanism? What about the SHARC prediction head? How does it combine with the other methods?

2. By "combining" SHARC with other methods, what's the network size increased? In general, we can expect improved performance for many tasks simply by increasing the network size. So it's important to know the increase of network size, after combining with SHARC.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
2 fair

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces Saliency-Guided Hidden Associative Replay for Continual Learning (SHARC), a method that attempts to tackle the catastrophic forgetting problem in continual learning by incorporating associative memory into replay-based strategies. The memory selectively stores essential feature map channels determined using saliency methods like Grad-CAM. Experiments on several benchmarks show improvements over some existing replay-based CL methods under task-incremental and class-incremental learning settings.

### Strengths
- The paper's endeavor to draw inspiration from insights into human brain function for addressing CL is commendable.

- The proposed method improves several existing replay-based CL methods.

### Weaknesses
1. The working mechanism of associative memory is confusing. 
- It is unclear how the queries are obtained during both training and inference. 
- The concept of queries, which appears to be image crops in Fig. 2, contradicts the notion presented in the paper, where specific feature map channels are retained.
- The practicality of recalling precisely the same image when given a query is questionable, as queries pertain to new classes, while the memory contents relate to old classes. This discrepancy, unless old queries are also stored, fundamentally undermines the approach. Storing old queries, however, introduces extra complexities that appear inconsistent with the intended advantages of using associative memory.


2. The reliance on gradient-based saliency methods to evaluate the importance of feature map channels may not align with the underlying feature selection mechanisms in the human brain.


3. The related work is noticeably lacking in depth. 
- The paper lacks a comprehensive overview of both regularization-based and dynamic architecture-based continual learning methods. Notably, there is a complete absence of references to the latter category.
- The review neglects to consider replay-based continual learning methods that store lightweight features or generate pseudo features for old classes [1-3], which should be addressed, discussed, and compared.
- The absence of a thorough examination of other continual learning methods employing brain-inspired memory systems, such as [4-5], leaves a critical gap that requires addressing through comprehensive review, discussion, and comparison.


4. In terms of comparisons: 
- It is unclear whether methods without SHARC in Tables I and II are also pre-trained on ImageNet. 
- The authors are encouraged to extend the comparison to include more recent methods introduced in 2022 or 2023.


5. The claim that "existing work Sun et al. (2015) has proved that hidden representation learned by convolutional neural networks is highly sparse in the hidden space" is inadequately supported, as the referenced work by Sun et al. (2015) predominantly focuses on face representations rather than general representations acquired through CNNs, rendering the argument questionable.

### Questions
- What is the value of K? Is it the same as the number of classes in order to perform the Grad-CAM? Will K change under the class-incremental setting?

- What are the two multiplication operations in Eq. (4), respectively?

- Is A’ a feature map after discarding the non-salient channels?

- Can you provide more explanations for the sentence “We only need to keep track of the channel index which is only a 1d vector and cheap to store”?

- What is the “partial cue” that is used to retrieve feature maps in the associative memory?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
