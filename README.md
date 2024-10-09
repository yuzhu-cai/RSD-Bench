# RSD-Bench: Requirement-Oriented Software Development Benchmark

[![paper](https://img.shields.io/badge/arXiv-Paper-<COLOR>.svg)](https://arxiv.org")

Code and data for paper "[Evolving Multi-Agent Collaboration Networks via Textual Backpropagation](https://arxiv.org)".

## 👋 Overview
RSD-Bench is a requirement-oriented benchmark designed to evaluate the ability of models to handle software-level coding tasks. Unlike instruction-based approaches, RSD-Bench uses detailed software requirements as input, specifying each functionality and constraint of the software. The benchmark includes automatic evaluation through unit tests, providing a more realistic assessment aligned with real-world software development practices.

<img src="assets/figs/evaluation.jpg">


## 🚀 Set Up

Make sure to use python 3.8 or later:
```
conda create -n rsd_bench python=3.8
conda activate rsd_bench
```

Check out and install this repository:
```
git clone https://github.com/yuzhu-cai/RSD-Bench.git
cd RSD-Bench
pip install -r requirement.txt
```

## 💽 Usage
> [!WARNING]
> **Operating System:** Ensure that you are running this project on an operating system with a graphical user interface. Currently, **Windows** and **macOS** are supported.
> 
> **Dependencies:** Make sure all dependencies are correctly installed and the appropriate Python environment is activated.

Use the following command to generate the software included in `RSD-Bench` using the GPT, Claude, or Gemini APIs. The generated code will be stored in the `codes` directory.

```bash
python run_infer.py
```

Evaluate the software code generated in the `codes` directory with the following command:

```bash
python run_eval.py
```

To aggregate the performance and differences of the software code generated under various settings, run:

```
python update_result.py
```


## ✍️ Citation

If you find our work helpful, please use the following citations.

```
[TODO]
```