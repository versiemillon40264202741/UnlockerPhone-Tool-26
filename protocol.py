class ProtocolHandler:
    @staticmethod
    def check_bootloader_status():
        # Verifying fastboot state
        state = subprocess.run(['fastboot', 'getvar', 'unlocked'], capture_output=True)
        return "unlocked" in state.stdout.decode()
