module top(
    input CLOCK_50,

    output [9:0] LEDR
    );

    reg [31:0] tickCounter = 0;

    always @(posedge CLOCK_50) begin
        tickCounter <= tickCounter + 1;
    end

    assign LEDR[9:0] = tickCounter[31:22];

endmodule
