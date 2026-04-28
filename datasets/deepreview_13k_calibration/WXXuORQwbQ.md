# Sparse Mask Representation for Human-Scene Interaction

- Decision: Reject
- Avg Score: 5.00
- Scores: 6, 6, 5, 3

## Abstract
Human-scene interaction is an active research topic with several applications in robotics, virtual experiences, gaming, surveillance, and healthcare. Despite efforts to improve the network architectures to achieve better results or optimize models for faster inference, a crucial aspect of input dimensionality has been somewhat overlooked. This paper introduces Sparse Mask Representation, a simple yet effective approach to enhance the inference speed of human-scene interaction models and improve the model's effectiveness by exploring the sparsity of high-dimensional inputs. Specifically, our method utilizes sparse masks to convert high-dimensional inputs into sparse tensors in a compressed COO format. Our approach not only effectively streamlines computational speed but also eliminates non-useful input information, thereby enhancing overall model performance. We conducted rigorous experiments across three datasets, with a specific emphasis on tasks related to contact prediction and scene synthesis. The results underscore the substantial enhancements realized by our proposed method in terms of accuracy and inference time, surpassing existing state-of-the-art approaches.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a new representation for human-scene interaction task. The authors suggest to inject sparsity in the input space rather than designing lightweight model, model pruning or quantization which were used by previous methods. By enforcing input sparsity, the method is simple and effective in benefitting both the accuracy and inference time.

### Strengths
* Proposed approach is very simple but effective. The design choices made by the authors are intuitive and make sense. 
* The experiments and analysis are quite comprehensive and provides insights for the method. 
* Discussion is fairly done and includes a number of limitations and future directions. Overall it is a well written research paper.

### Weaknesses
 * Methodology is incremental and not much novelty by itself.

### Questions
I can see that from Figure 6. it shows optimal performance for k = 3 mask with 90% sparsity, but there is no clear pattern or correlation between sparsity ratio vs accuracy. Could authors give an explanation on this trend?

### Soundness
2 fair

### Presentation
3 good

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
The paper introduces a novel approach called Sparse Mask Representation (SMR) to effectively handle the complex and sparse input data in human-scene interaction. Unlike previous methods that focused on lightweight models or quantization, SMR uses sparse masks to select important information from the input, reducing computational cost. Experimental results demonstrate its superior performance in contact prediction and scene synthesis tasks, with significantly faster inference speed.

### Strengths
The paper is skillfully written, ensuring ease of comprehension for the reader. It introduces a seemingly straightforward yet remarkably effective solution to the complex issue of human contact prediction in 3D environments. The authors have undertaken a thorough set of experiments, clearly demonstrating the superior performance of their approach. Furthermore, they have meticulously examined the related work, providing a comprehensive comparison with existing literature across multiple datasets.

### Weaknesses
I find the paper to be well-written, and the authors have conducted thorough experiments to demonstrate the effectiveness of their approach. The only potential area for improvement lies in providing more detailed explanations on how the sparse masks are defined, especially in the context of task dependency. This would further enhance the clarity and depth of the paper.

### Questions
Are the sparse masks randomly generated, meaning do the 0 and 1 values occur at random locations? Or are the masks specifically tailored to the task at hand?

How does your approach handle fine-grained contacts, such as situations where the tips of the fingers come into contact with other objects?

Additionally, could you elaborate on how your approach addresses videos?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
Instead of focusing on optimizing the model architecture, the authors proposed a novel way to enhance the human-scene interaction research from the view of representation. 
It is revealed that the input for human-scene interaction is usually of high dimension, which limits the inference speed and effectiveness of the models.
Sparse Mask Representation is thus proposed, exploring the sparsity of the inputs.
Rigorous experiments are conducted on tasks related to contact prediction and scene synthesis.
Results show the effectiveness of the proposed sparse encoding.

### Strengths
The authors show that introducing sparse encoding is an effective technique for the improvement of Human-Scene Interaction tasks.
Impressive inference acceleration and model compression are achieved with the proposed method.
Competitive results are shown compared to previous efforts.

### Weaknesses
The current version appears to be an application of the Choy, 2020 citation. Clarification on the contribution beyond this should be provided.

As mentioned, the acceleration could be attributed to two factors. First, a sparse body mesh with 90% fewer vertices is used. Second, the sparse network works. Ablation should be conducted on the sparse mesh only and the sparse network only.

### Questions
Please refer to the Weaknesses section.

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes the use of sparse tensors to represent human-scene interaction data. Given a dense tensor input the authors proposed to learn multiple sparse masks. Sparse tensors are created by multiplying the learned masks and the dense input tensor. The sparse masks have a pre-defined fixed sparsity. The authors reused existing dense architecture but converted its dense operations into sparse ones.
The paper shows two applications: contact prediction and scene generation

### Strengths
- The input dimensionality in human-scene interaction is rightfully large. Using sparse input for this task is novel and technically sound.
- The paper is easy to read.
- Human-scene interaction is an interesting and important problem.

### Weaknesses
 - The novelty is limited to sparsifying the input for the human-scene interaction. Using sparse inputs by itself is not new, but it has not been studied for this task before.
- In Figure 6 and Table 4. It seems the model gets worse when using 50 or 10 masks which is strange.Why would using 3 masks be better than 10 or 50 masks? Why would it be even better than using the full dense tensor?
- The paper attributes the COO representation to "Choy 2020". The COO format is much older than that. 
- Figure 4 is hard to see. Human bodies are too small.

### Questions
- The method is basically learning mesh subsampling. I wonder about how the method compares to classic subsampling methods.
- Did the masking learn any interesting patterns? like which vertices are more relevant for which pose?
- I understand that the method can be faster than POSA, but why would it be more accurate?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
1 poor
