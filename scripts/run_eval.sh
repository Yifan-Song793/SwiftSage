# DEBUG_MODE="-m debugpy --listen 127.0.0.1:5679 --wait-for-client"

python $DEBUG_MODE -m swiftsage.evaluate_benchmark \
    --swift_api_provider vLLM \
    --swift_model_id /home/yifan/models/Llama-3.1-8B-Instruct \
    --dataset_name math-l5 \
    --prompt_template_dir ./swiftsage/prompt_templates \
    --num_test_sample 10 \

# python $DEBUG_MODE -m swiftsage.evaluate_benchmark \
#     --dataset_name gpqa \
#     --prompt_template_dir ./swiftsage/prompt_templates \
#     --num_test_sample 4 \
