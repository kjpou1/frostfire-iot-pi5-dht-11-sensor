import asyncio
import logging
from app.config import Config
from app.models.command_line_args import CommandLineArgs
from app.services.things_data_publisher import ThingsDataPublisher

class Host:
    def __init__(self, args: CommandLineArgs):
        """
        Initialize the Host class with command line arguments and configuration.

        Parameters:
        args (CommandLineArgs): Command line arguments passed to the script.
        """
        self.args = args
        self.config = Config()
        self.logger = logging.getLogger(__name__)
        self.publisher = ThingsDataPublisher(self.config)

    def run(self):
        """
        Run the asynchronous run_async method.
        """
        return asyncio.run(self.run_async())

    async def run_async(self):
        """
        Asynchronous method to perform the main logic.
        """
        self.logger.info("Starting host process.")
        try:
            await self.publisher.start()
        except Exception as e:
            self.logger.error(f"An error occurred: {e}")

if __name__ == '__main__':
    # Setup logging configuration
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

    # Example usage, adjust how args are passed in your actual implementation
    args = CommandLineArgs()
    host = Host(args)
    host.run()
