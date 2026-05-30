module uart_tx (
    input clk,
    input rst,
    input start,
    input [7:0] data_in,
    output reg tx,
    output reg done
);

    parameter IDLE  = 2'b00;
    parameter START = 2'b01;
    parameter DATA  = 2'b10;
    parameter STOP  = 2'b11;

    reg [1:0] state;
    reg [2:0] bit_index;

    always @(posedge clk or posedge rst) begin
        if (rst) begin
            state     <= IDLE;
            tx        <= 1'b1;
            done      <= 1'b0;
            bit_index <= 0;
        end else begin
            case (state)
                IDLE: begin
                    tx   <= 1'b1;
                    done <= 1'b0;
                    if (start)
                        state <= START;
                end

                START: begin
                    tx    <= 1'b0;
                    state <= DATA;
                    bit_index <= 0;
                end

                DATA: begin
                    tx <= data_in[bit_index];
                    if (bit_index == 7)
                        state <= STOP;
                    else
                        bit_index <= bit_index + 1;
                end

                STOP: begin
                    tx    <= 1'b1;
                    done  <= 1'b1;
                    state <= IDLE;
                end
            endcase
        end
    end

endmodule
