// ViewHolder code for RecyclerView
package com.example.agile_control;

import android.view.View;
import android.widget.TextView;

import androidx.recyclerview.widget.RecyclerView;

public class ChannelViewHolder
		extends RecyclerView.ViewHolder {
	TextView channelName;
	TextView channelState;
	View view;

	ChannelViewHolder(View itemView)
	{
		super(itemView);
		channelName
				= (TextView)itemView
				.findViewById(R.id.channelName);
		channelState
				= (TextView)itemView
				.findViewById(R.id.channelState);
		view = itemView;
	}
}
