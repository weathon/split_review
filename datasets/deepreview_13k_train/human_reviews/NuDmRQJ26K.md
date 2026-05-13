# LUMEN-PRO: Automating Multi-Task Learning on Optical Neural Networks with Weight Sharing and Physical Rotation

- Decision: Reject
- Scores: 3, 6, 8

## Abstract
With the demise of Moore's law, the demand for efficient deep neural network accelerators has surged. In addition, the democratization of AI encourages multi-task learning (MTL), demanding more parameters and processing time. To achieve highly energy-efficient MTL, Diffractive Optical Neural Networks (DONNs) have garnered attention due to extremely low energy and high computation speed. However, implementing MTL on DONNs requires manually reconfiguring and replacing specific layers, resulting in rebuilding and duplicating the physical systems. To overcome the challenges, we propose LUMEN-PRO, an automating MTL framework. Specifically, we first propose to automate MTL utilizing an arbitrary backbone DONN and a set of tasks, resulting in a high-accuracy multi-task DONN model with a small memory footprint that surpasses existing MTL methods. Secondly, we leverage the rotatability of the physical system, and replace task-specific layers with the rotation of the corresponding shared layers. This replacement eliminates the storage requirement of task-specific layers, thus further optimizing the memory footprint. LUMEN-PRO provides flexibility in identifying optimal sharing patterns across diverse datasets, facilitating the search for highly energy-efficient DONNs. Experimental results show that LUMEN-PRO provides up to 49.58% higher accuracy and $4\times$ better cost efficiency than single-task and existing cutting-edge DONN approaches on different datasets. It achieves memory lower bound of multi-task learning, i.e., having the same memory storage as the single task model. Compared to technologies such as IBM TrueNorth and Nanophotonic, LUMEN-PRO achieves $10^5\times$ and $10\times$ speedup in throughput, and $5,969\times$ and $680\times$ energy efficiency gain, respectively.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work describes a multi-task learning approach for a specific optical neural network named Diffractive Optical Neural Networks (DONN). It leverages the rotability of the physical system to share the same module across different tasks. Experiments was conducted on MNIST and its variants, and a face attribute dataset. The proposed method is able to outperform existing DONN multi-task learning method on accuracy with lower cost to fabricate the system.

### Strengths
-	The idea of enabling layer sharing in a optical neural network is interesting. The authors use some existing gradient-based architecture search algorithm (Automtl Neurips 22) and adapt it to the DONN scenario.
-	The proposed method achieves significant performance gain on MNIST and Celeb-Faces dataset compared to existing multi-task methods such as VanillaMT and RubikONN.

### Weaknesses
 - The application of designing multi-task learning method for the DONN is too narrow. DONN is just one type of optical neural network and there is no evidence that this approach generalizes to other physical neural networks. The method may not have much practical usages in real life.
- The experiments conducted seems only from a mathematical perspective. If we put this solution to produce physical systems, will there be accuracy degeneration due to imperfect fabrication? And is the proposed rotation-based sharing method practical in real fabricated system? The authors did not address these issues.
- Due to my lack of experience with this field, I do not understand a lot of technical details in this work. I believe the authors can improve on the explanation of the key concept to make it easy to understand. For example, the Figure 3 is really confusing. What does a node mean? What does the numbers in the node blocks mean? Are they network weights? There are a bunch of switches on the figure. What is the functionality of these switches and how do they work? Another key concept is the rotation-based layer sharing. What exactly does rotation mean in this scenario? How does such rotation facilitate weight sharing?
- Table 3 is kind of confusing. It seems to contain both ASIC-based solution and physical neural networks. How do you measure the throughput of an optical neural network? The proposed framework has very high throughput but is it really possible in a real system? Since you need to switch the input image physically at such a fast rate. And what does ``Accuracy’’ mean in this table? Is it just the testing accuracy on MNIST?

### Questions
-	Table 3 is kind of confusing. It seems to contain both ASIC-based solution and physical neural networks. How do you measure the throughput of an optical neural network? The proposed framework has very high throughput but is it really possible in a real system? Since you need to switch the input image physically at such a fast rate. And what does ``Accuracy’’ mean in this table? Is it just the testing accuracy on MNIST?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a multi-task learning optical neural network framework, LUMEN-PRO, which uses the physical principles to effectively improve the performance and cost of the model for multi-tasks.

### Strengths
1. The idea of modeling multitasking by rotating the physical layer is novel and interesting and can effectively reduce costs.

2. Diffractive optical neural networks-based methods can greatly improve the inference performance.

3. This area of research is rare and can increase the diversity of the ML community.

### Weaknesses
1. The method depends on the rotation of the physical layer. However, the physical layer has at most four directions. Therefore, the method only supports most four tasks.

2. The method is mainly derived from the AutoMTL [1] method.

3. The presentation is not clear enough. Some details are not included in the paper. This can be seen in the questions.

4. The Figures are not annotated; thus, it is difficult to understand the method directly by looking at them.

### Questions
1. What is the meaning of the  LUMEN-PRO in Figure 5? As I understand, this network can only make the inference function different under different tasks by rotating the layers.

2. Why the LUMEN-PRO’s performance can exceed the single task in Figure 5? Normally, it works best to use a separate model for each task.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes an automated multi-task learning (MTL) framework dubbed LUMEN-PRO dedicated to diffractive optical neural networks (DONN). Then, the authors leverage the rotatability of the physical system and replace task-specific layers with the rotation of the corresponding shared layers. Both effectively reduce the memory footprint.

Experiments also show that the proposed LUMEN-PRO provides up to 49.58% higher accuracy and 4x better cost efficiency than single task and prior art methods.

### Strengths
1. The paper organization is great. Even though I do not have a relevant background on DONN, I can still follow the logic to understand the paper. E.g., Table 1 provides a good summary of current MTL methods and how the proposed one is better or more comprehensive.

2. The proposed method leverages the rotatability of the physical system to fine-tune the multi-task DONN. It is like the spatial shift to CNNs and helps with the generalization ability learning of such models.

3. Experiments show that the proposed methods achieve better task accuracy and cost efficiency than previous methods.

### Weaknesses
I am not an expert on DONN. As for the MTL and NAS:

The idea sounds like a combination of NAS and MTL. What is unique here for DONN? Is this method the general method that can be applied to other CNN or Transformer models?

You mentioned that the rotation mechanism has a physical meaning, what is that? Why is the rotation different from spatial shifts in CNNs?

As for the experiments, MNIST and CelebA are relatively small datasets, why do you consider larger ones? Is that because such DONN has some generalization or scalability issue preventing it from adapting to large scales?

### Questions
See Weaknesses

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
