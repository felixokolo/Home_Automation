package com.example.agile_control;

import android.content.Context;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;

import androidx.recyclerview.widget.RecyclerView;

import java.util.Collections;
import java.util.List;

public class ChannelListAdapter
		extends RecyclerView.Adapter<ChannelViewHolder> {

	List<ChannelData> list;

	Context context;
	ClickListiner listiner;

	public ChannelListAdapter(List<ChannelData> list,
								Context context,ClickListiner listiner)
	{
		this.list = list;
		this.context = context;
		this.listiner = listiner;
	}

	@Override
	public ChannelViewHolder
	onCreateViewHolder(ViewGroup parent,
					   int viewType)
	{

		Context context
				= parent.getContext();
		LayoutInflater inflater
				= LayoutInflater.from(context);

		// Inflate the layout

		View photoView
				= inflater
				.inflate(R.layout.channel_card,
						parent, false);

		ChannelViewHolder viewHolder
				= new ChannelViewHolder(photoView);
		return viewHolder;
	}

	@Override
	public void
	onBindViewHolder(final ChannelViewHolder viewHolder,
					 final int position)
	{
		final int index = viewHolder.getAdapterPosition();
		viewHolder.channelName
				.setText(list.get(position).name);
		viewHolder.channelState
				.setText(list.get(position).state);
		viewHolder.view.setOnClickListener(new View.OnClickListener() {
			@Override
			public void onClick(View view)
			{
				listiner.click(index);
			}
		});
	}

	@Override
	public int getItemCount()
	{
		return list.size();
	}

	@Override
	public void onAttachedToRecyclerView(
			RecyclerView recyclerView)
	{
		super.onAttachedToRecyclerView(recyclerView);
	}


}

